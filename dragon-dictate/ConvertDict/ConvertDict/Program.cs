﻿namespace ConvertDict
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputFilename = @"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\dragon-dictate\SYSTEM.DDX";
            string tempFilename = @"c:\temp\talon\dictation.talon";
            string outputFilename = @"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\talon-customisation\system.talon";

            string[] inputLines = File.ReadAllText(inputFilename).Split("\r\n");
            Parser parser = new Parser();
            /* List<string> attributeList = parser.GetAttributeList(inputLines);
            string str = String.Join("\r\n", attributeList); */

            List<ParseEntity> parseEntityList = parser.Parse(inputLines);
            string str = String.Join("\r\n", parseEntityList.Select(i => i.TalonFormat()));
            File.WriteAllText(tempFilename, str);

            File.Copy(tempFilename, outputFilename, overwrite: true);
        }
    }
}
