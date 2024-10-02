using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class KeysConverter
    {
        public static void Convert(string ddKeys, out string talonKeys, out bool hasVirtualKeys)
        {
            ddKeys = Util.RemoveSurroundingQuotes(ddKeys);
            StringBuilder sb = new StringBuilder();
            int i = 0;
            hasVirtualKeys = false;
            while (i < ddKeys.Length)
            {
                char c = ddKeys[i];
                if (c == '{')
                {
                    int end = ddKeys.IndexOf('}', i);
                    if (end == -1)
                        sb.Append(c);
                    else
                    {
                        int length = end - i + 1;
                        string virtualKey = ddKeys.Substring(i, length);
                        sb.Append(ConvertSingleKey(virtualKey));
                        hasVirtualKeys = true;
                        i = end;
                    }
                }
                else
                    sb.Append(c);

                i++;
            }
            talonKeys = sb.ToString();
        }

        public static string ConvertSingleKey(string virtualKey)
        {
            string str = virtualKey.ToLower();
            str = str.Replace("ext", "");
            str = str.Replace("+", "-");
            return str;
        }
    }
}
