using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class ScriptConverter
    {
        private static Dictionary<string, string> modeDict = new Dictionary<string, string>(){
            { "1", "{Z1}" }, 
            { "2", "{Z1L}" },
            { "4", "{Z4}" }
        };

        public static string Convert(List<string> parts, ref int idx)
        {
            StringBuilder sb = new StringBuilder();

            while (idx < parts.Count - 1)
            {
                string cmd = parts[idx].ToLower();
                if (cmd == "")
                {
                    idx++;
                    continue;
                }
                if ((cmd == "shellexecute") ||
                    (cmd == "buttonclick") ||
                    (cmd == "menupick") ||
                    (cmd == "msgboxconfirm") ||
                    (cmd == "resetgroup"))
                {
                    return "";
                }

                string param = parts[idx + 1];
                if (cmd.StartsWith('/'))
                    break;
                    
                string? str = ConvertLine(cmd, param);
                if (str != null)
                    sb.Append(str);

                idx += 2;
            }
            return sb.ToString();
        }

        private static string? ConvertLine(string cmd, string param)
        {
            string? result = null;
            switch (cmd.ToLower())
            {
                case "sendkeys":
                    result = Util.RemoveSurroundingQuotes(param);
                    break;

                case "capitalizenext":
                    {
                        if (modeDict.ContainsKey(param))
                        {
                            result = modeDict[param];
                        }
                        break;
                    }

                case "capitalizebegin":
                    break;

                case "wait":
                    result = "{wait:" + param + "}";
                    break;

                case "heardword":
                    result = "{heardword:" + param + "}";
                    break;

                case "nospacenext":
                case "nospacebegin":
                case "rejectpreviousword":
                case "shellexecute":
                    break;

                default:
                    throw new Exception();
            }
            return result;
        }


        private static bool SplitCommand(string str, out string cmd, out string param)
        {
            str = str.Trim();
            bool result = str.Length > 1;
            cmd = param = "";
            int pos = 0;
            if (result)
            {
                pos = str.IndexOf(" ");
                result = (pos > 0) && (pos < str.Length - 1);
            }
            if (result)
            {
                cmd = str.Substring(0, pos);
                param = str.Substring(pos + 1).Trim();
            }
            return result;
        }
    }
}
