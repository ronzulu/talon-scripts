using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class Parser
    {
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
            bool isMidQuote = false;
            for (int i = 0; i < lines.Length; i++)
            {
                string line = lines[i];
                if (line.ToUpper().Contains("[D. E. C. 22]"))
                    isMidQuote = isMidQuote;
                (List<string> singleStringList, bool nowMidQuote) = ParseSingleLine(line);
                if (isMidQuote)
                {
                    stringList.AddRange(singleStringList);
                }
                else
                {
                    stringList = singleStringList;
                }
                if (!nowMidQuote)
                {
                    result.Add(new Macro(new List<string>(stringList)));
                    stringList.Clear();
                }
                isMidQuote = nowMidQuote;
            }
            return result;
        }

        private (List<string> singleStringList, bool midQuote) ParseSingleLine(string line)
        {
            List<string> result = new List<string>();
            bool midQuote = false;
            bool midEscape = false;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < line.Length; i++)
            {
                char c = line[i];
                if (midEscape)
                {
                    sb.Append(c);
                    midEscape = false;
                }
                else if (c == '\\')
                    midEscape = true;
                else if (c == '"')
                {
                    sb.Append(c);
                    midQuote = !midQuote;
                }
                else if (!midQuote && Char.IsWhiteSpace(c))
                {
                    if (sb.Length > 0)
                    {
                        result.Add(sb.ToString());
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

            return (result, midQuote);
        }
    }

    public class ParseEntity
    {
        public string Word { get; set; }
        public string Keys { get; set; }

        public ParseEntity(string word, string keys)
        {
            Word = word;
            Keys = keys;
        }

        public override string ToString()
        {
            return $"{Word}: \"{Keys}\"";
        }
    }
}
