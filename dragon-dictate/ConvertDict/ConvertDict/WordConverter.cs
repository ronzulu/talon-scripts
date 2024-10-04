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
            string result;
            if (int.TryParse(str, out var v))
                result = ConvertNumberToTalon(v);
            else 
                result = str;
            return result;
        }

        private static string ConvertNumberToTalon(int num)
        {
            string result;
            if ((num >= 0) && (num <= 19))
                result = ConvertSmallNumberToTalon(num);
            else if (num <= 99)
            {
                int tens = (num / 10) * 10;
                string tensStr = tens switch
                {
                    20 => "twenty",
                    30 => "thirty",
                    40 => "forty",
                    50 => "fifty",
                    60 => "sixty",
                    70 => "seventy",
                    80 => "eighty",
                    90 => "ninety",
                    _ => throw new Exception()
                };
                result = tensStr;
                int digit = num % 10;
                if (digit > 0)
                    result += " " + ConvertSmallNumberToTalon(digit);
            }
            else if (num <= 9999)
            {
                int hundreds = (num / 100);
                int mod = (num % 100);
                result = ConvertNumberToTalon(hundreds);
                result += (hundreds < 10) ? " hundred" : " [hundred]";
                if (mod > 0)
                {
                    if (mod <= 9)
                        result += " [zero]";
                    result += $" {ConvertNumberToTalon(mod)}";
                }
            }
            else
                result = num.ToString();

            return result;
        }

        private static string ConvertSmallNumberToTalon(int num) => num switch
        {
            0 => "zero",
            1 => "one",
            2 => "two",
            3 => "three",
            4 => "four",
            5 => "five",
            6 => "six",
            7 => "seven",
            8 => "eight",
            9 => "nine",
            10 => "ten",
            11 => "eleven",
            12 => "twelve",
            13 => "thirteen",
            14 => "fourteen",
            15 => "fifteen",
            16 => "sixteen",
            17 => "seventeen",
            18 => "eighteen",
            19 => "nineteen",
            _ => throw new Exception()
        };
    }
}
