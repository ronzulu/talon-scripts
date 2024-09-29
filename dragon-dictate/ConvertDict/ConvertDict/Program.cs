namespace ConvertDict
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputFilename = @"C:\Users\ronny\AppData\Roaming\talon\user\talon-scripts\dragon-dictate\DICTATIO.DDX";
            string outputFilename = @"c:\temp\talon\dictation.talon";

            string[] inputLines = File.ReadAllText(inputFilename).Split("\r\n");
            Parser parser = new Parser();
            List<ParseEntity> parseEntityList = parser.Parse(inputLines);
            string str = String.Join("\r\n", parseEntityList.Select(i => i.ToString()));
            File.WriteAllText(outputFilename, str);
        }
    }
}
