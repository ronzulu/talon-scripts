using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    internal class Parser
    {
        public Parser() { }

        public List<ParseEntity> Parse(string[] lines)
        {
            List<ParseEntity> result = new List<ParseEntity>();
            List<List<string>> macroList = MacroParser(lines);
            foreach (var macro in macroList)
            {
                ParseEntity? entity = ParseMacro(macro);
                if (entity != null)
                {
                    result.Add(entity);
                }
            }
            return result;
        }

        private ParseEntity? ParseMacro(List<string> macro)
        {
            ParseEntity? result = null;
            if (macro.Count == 4)
            {
                if ((macro[0] == "add-word") &&
                (macro[1].Length > 2) && 
                (macro[2] == "/keys") &&
                (macro[3].Length > 0))
                {
                    string? rule = ConvertDragonWordToTalonRule(macro[1]);
                    if (rule != null)
                    {
                        result = new ParseEntity(rule, macro[3]);
                    }
                }
            }
            return result;
        }

        private static string? ConvertDragonWordToTalonRule(string word)
        {
            string? result = null;
            if (word.StartsWith('[') && word.EndsWith(']'))
            {
                word = word.Substring(1, word.Length - 2).Replace(".", "");
                string[] substringList = word.ToLower().Split(" ");
                if (substringList.All(i => i.Length == 1))
                    result = String.Join(" ", substringList);

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
        public List<List<string>> MacroParser(string[] lines)
        {
            List<List<string>> result = new List<List<string>>();
            List<string> stringList = new List<string>();
            bool isMidQuote = false;
            for (int i = 0; i < lines.Length; i++)
            {
                string line = lines[i];
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
                    result.Add(new List<string>(stringList));
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
                    midQuote = !midQuote;
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
