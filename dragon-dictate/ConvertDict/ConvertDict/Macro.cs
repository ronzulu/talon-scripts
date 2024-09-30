using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class Macro
    {
        public List<string> strList = new List<string>();

        public Macro(List<string> strList)
        {
            this.strList = strList;
        }

        public HashSet<string> GetAttributeList()
        {
            HashSet<string> set = new HashSet<string>();
            foreach (var str in strList)
            {
                if (str.StartsWith("/"))
                    set.Add(str);
            }
            return set;
        }

        public ParseEntity? Parse()
        {
            ParseEntity? result = null;
            if (strList.Count >= 4)
            {
                if ((strList[0] == "add-word") &&
                IsSurroundedByQuotes(strList[1]) &&
                (strList[2] == "/keys") &&
                (strList[3].Length > 0))
                {
                    string? rule = ConvertDragonWordToTalonRule(strList[1]);
                    if (rule != null)
                    {
                        // string str = strList[3].Substring(1, strList[3].Length - 2);
                        result = new ParseEntity(rule, RemoveSurroundingQuotes(strList[3]));
                    }
                }
            }
            return result;
        }

        private static bool IsSurroundedByQuotes(string str) 
        {
            return (str.Length > 2) && str.StartsWith('"') && str.EndsWith('"');
        }

        private static string RemoveSurroundingQuotes(string str)
        {
            return IsSurroundedByQuotes(str) ? str.Substring(1, str.Length - 2) : str;
        }

        private static string? ConvertDragonWordToTalonRule(string word)
        {
            string? result = null;
            if (word == "\"[D. E. C. 22]\"")
                result = null;
            if (word.StartsWith("\"[") && word.EndsWith("]\""))
            {
                word = word.Substring(2, word.Length - 4).Replace(".", "");
                string[] substringList = word.ToLower().Split(" ");
                result = String.Join(" ", substringList.Select(i => ConvertStringToTalon(i)));

            }
            return result;
        }

        private static string ConvertStringToTalon(string str)
        {
            return (str.Length == 1) ? ConvertCharToTalon(str[0]) : str;
        }

        private static string ConvertCharToTalon(char ch) => ch switch
        {
            '0' => "zero",
            '1' => "one",
            '2' => "two",
            '3' => "three",
            '4' => "four",
            '5' => "five",
            '6' => "six",
            '7' => "seven",
            '8' => "eight",
            '9' => "nine",
            _ => ch.ToString()
        };
    }
}
