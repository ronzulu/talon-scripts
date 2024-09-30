namespace ConvertDict
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputFilename = @"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\dragon-dictate\DICTATIO.DDX";
            string tempFilename = @"c:\temp\talon\dictation.talon";
            string outputFilename = @"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\talon-customisation\dictation.talon";

            string[] inputLines = File.ReadAllText(inputFilename).Split("\r\n");
            Parser parser = new Parser();
            List<ParseEntity> parseEntityList = parser.Parse(inputLines);
            string str = String.Join("\r\n", parseEntityList.Select(i => i.ToString()));
            File.WriteAllText(tempFilename, str);

            File.Copy(tempFilename, outputFilename, overwrite: true);
        }
    }
}
