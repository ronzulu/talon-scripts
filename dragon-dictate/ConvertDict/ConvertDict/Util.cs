using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    internal class Util
    {

        public static bool IsSurroundedByQuotes(string str)
        {
            return (str.Length > 2) && str.StartsWith('"') && str.EndsWith('"');
        }

        public static string RemoveSurroundingQuotes(string str)
        {
            return IsSurroundedByQuotes(str) ? str.Substring(1, str.Length - 2) : str;
        }
    }
}
