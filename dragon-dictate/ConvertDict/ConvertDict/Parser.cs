using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class Parser
    {
        private bool midScript = false;

        public Parser() { }

        public List<string> GetAttributeList(string[] lines)
        {
            HashSet<string> set = new HashSet<string>();
            List<Macro> macroList = MacroParser(lines);
            foreach (var macro in macroList)
            {
                set.Union(macro.GetAttributeList());
            }
            var result = from s in set
                orderby s
                select s;
            return result.ToList();
        }

        public List<ParseEntity> Parse(string[] lines)
        {
            List<ParseEntity> result = new List<ParseEntity>();
            List<Macro> macroList = MacroParser(lines);
            foreach (var macro in macroList)
            {
                ParseEntity? entity = macro.Parse();
                if (entity != null)
                {
                    result.Add(entity);
                }
                else
                {
                    int i = 0; 
                }
            }
            return result;
        }

        /* 
         * 
            add-word "[Power Of 3]" /keys ^3 /nsc
            add-word "[Power Shell Admin]" /script "SendKeys \"Powershell\"
            HeardWord \"[M. Right]\"" /nsc
            add-word "[Power User 1]" /keys PowerUser

         */
        public List<Macro> MacroParser(string[] lines)
        {
            List<Macro> result = new List<Macro>();
            List<string> stringList = new List<string>();
            int quoteDepth = 0;
            midScript = false;
            for (int i = 0; i < lines.Length; i++)
            {
                string line = lines[i];
                int newQuoteDepth = quoteDepth;
                ParseSingleLine(line, ref newQuoteDepth, out List<string> singleStringList);
                if (quoteDepth > 0)
                {
                    stringList.Add("");
                    stringList.AddRange(singleStringList);
                }
                else
                {
                    stringList = singleStringList;
                }
                if (newQuoteDepth == 0)
                {
                    result.Add(new Macro(new List<string>(stringList)));
                    stringList.Clear();
                }
                quoteDepth = newQuoteDepth;
            }
            return result;
        }

        private void ParseSingleLine(string line, ref int quoteDepth, out List<string> singleStringList)
        {
            List<string> result = new List<string>();
            bool midEscape = false;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < line.Length; i++)
            {
                char c = line[i];
                if (midEscape)
                {
                    sb.Append(c);
                    midEscape = false;
                    if (c == '"')
                        quoteDepth = (quoteDepth == 2) ? 1 : (quoteDepth + 1);
                }
                else if (c == '\\')
                    midEscape = true;
                else if (c == '"')
                {
                    quoteDepth = (quoteDepth == 0) ? 1 : 0;
                    if (quoteDepth == 0)
                        midScript = false;
                }
                else if (((quoteDepth == 0) || ((quoteDepth == 1) && midScript)) && 
                    Char.IsWhiteSpace(c))
                {
                    if (sb.Length > 0)
                    {
                        result.Add(sb.ToString());
                        if (sb.ToString().ToLower() == "/script")
                            midScript = true;
                        sb = new StringBuilder();
                    }
                }
                else
                {
                    sb.Append(c);
                }
            }
            if (sb.Length > 0)
                result.Add(sb.ToString());

            singleStringList = result;
        }
    }

    public class ParseEntity
    {
        public string Word { get; set; }
        public string Keys { get; set; }
        public List<string> AttributeList { get; set; }
        public bool HasVirtualKeys { get; set; }
        public bool IsScript { get; set; }

        public ParseEntity(string word, string keys, bool hasVirtualKeys)
        {
            Word = word;
            Keys = keys;
            HasVirtualKeys = hasVirtualKeys;
            AttributeList = new List<string>();
        }

        public override string ToString()
        {
            return $"{Word}: \"{Keys}\"";
        }

        public string TalonFormat()
        {
            string result = $"{Word}: ";
            if (IsScript)
            {
                // Make braces double, for python
                string keys = Keys.Replace("{", "{{").Replace("}", "}}");
                result += $"user.rz_insert_key_sequence(\"{keys}\")";
            }
            else if (HasVirtualKeys)
            {
                // Make braces double, for python
                string keys = Keys.Replace("{", "{{").Replace("}", "}}");
                result += $"user.rz_insert_key_sequence(\"{keys}\")";
            }
            else
                result += $"\"{Keys}\"";
            return result;
        }
    }
}
