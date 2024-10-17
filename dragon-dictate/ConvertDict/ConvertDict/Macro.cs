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
                    (strList[1].Length > 0) &&
                    (strList[3].Length > 0))
                {
                    string? rule = WordConverter.ConvertDragonWordToTalonRule(strList[1]);
                    if (rule != null)
                    {
                        int idx = 3;
                        switch (strList[2]) 
                        {
                            case "/keys":
                                KeysConverter.Convert(strList[idx++], out string talonKeys, out bool hasVirtualKeys);
                                result = new ParseEntity(rule, talonKeys, hasVirtualKeys);
                                break;

                            case "/script":
                                {
                                    talonKeys = ScriptConverter.Convert(strList, ref idx);
                                    result = new ParseEntity(rule, talonKeys, false);
                                    result.IsScript = true;
                                    break;
                                }

                            default:
                                break;
                        }
                        if (result != null)
                        {
                            result.AttributeList = strList.ToList().Skip(idx).ToList();
                        }
                    }
                }
            }
            return result;
        }
    }
}
