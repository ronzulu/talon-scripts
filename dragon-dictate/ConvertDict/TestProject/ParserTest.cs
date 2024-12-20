using ConvertDict;

namespace TestProject
{
    public class ParserTest
    {
        private static char q = '"';

        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
            List<string> expectedAttributes = new List<string>();
            TestSingle($"add-word {q}[D. D. K.]{q} /keys DDK", "d d k", "DDK", expectedAttributes);
        }

        [Test]
        public void Test2()
        {
            List<string> expectedAttributes = new List<string>();
            TestSingle($"add-word {q}[D. D. K. 6]{q} /keys DDK", "d d k six", "DDK", expectedAttributes);
        }

        [Test]
        public void Test3()
        {
            List<string> expectedAttributes = new List<string>();
            TestSingle($"add-word {q}[Active Directory]{q} /keys {q}Active Directory{q}", "active directory", "Active Directory", expectedAttributes);
        }

        [Test]
        public void Test4()
        {
            string input = @"add-word ""[C. New Block]"" /keys {{Enter}{Enter}}{Up}{End}{Tab} /nsc";
            List<string> expectedAttributes = new List<string>() { "/nsc" };

            TestSingle(input, "c new block", "{l-brace}{enter}{enter}{r-brace}{up}{end}{tab}", expectedAttributes);
        }

        [Test]
        public void Test100()
        {
            string input = @"add-word ""[B. Plus L.]"" /script ""SendKeys \"" + \""
CapitalizeNext 2"" /nsc";
            List<string> expectedAttributes = new List<string>() { "/nsc" };

            TestSingle(input, "b plus l", " + {Z1L}", expectedAttributes);
        }

        private void TestSingle(string input, string expectedWord, string expectedKeys, List<string> expectedAttributes) 
        {
            string[] inputLines = input.Split("\r\n");
            Parser parser = new Parser();
            List<ParseEntity> result = parser.Parse(inputLines);
            Assert.That(result.Count, Is.EqualTo(1));
            Assert.That(result[0].Word, Is.EqualTo(expectedWord));
            Assert.That(result[0].Keys, Is.EqualTo(expectedKeys));
            Assert.That(result[0].AttributeList, Is.EqualTo(expectedAttributes));
        }
    }
}