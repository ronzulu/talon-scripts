using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConvertDict
{
    public class WordConverter
    {

        public static string? ConvertDragonWordToTalonRule(string word)
        {
            string? result = null;
            if (word.StartsWith("[") && word.EndsWith("]"))
            {
                word = word.Substring(1, word.Length - 2).Replace(".", "");
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
