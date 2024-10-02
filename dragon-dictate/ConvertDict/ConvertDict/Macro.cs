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
                Util.IsSurroundedByQuotes(strList[1]) &&
                (strList[2] == "/keys") &&
                (strList[3].Length > 0))
                {
                    string? rule = WordConverter.ConvertDragonWordToTalonRule(strList[1]);
                    if (rule != null)
                    {
                        // string str = strList[3].Substring(1, strList[3].Length - 2);
                        result = new ParseEntity(rule, Util.RemoveSurroundingQuotes(strList[3]));
                    }
                }
            }
            return result;
        }
    }
}
