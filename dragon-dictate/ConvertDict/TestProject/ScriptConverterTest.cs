using ConvertDict;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject
{
    public class ScriptConverterTest
    {
        [Test]
        public void Test001()
        {
            List<string> input = new List<string>(){ "SendKeys", "where ", "", "CapitalizeNext", "2" };
            TestSingle(input, 0, "where {Z1L}", 5);
        }

        private void TestSingle(List<string> input, int startIdx, string expectedScript, int expectedEndIdx)
        {
            int idx = startIdx;
            string actual = ScriptConverter.Convert(input, ref idx);
            Assert.That(actual, Is.EqualTo(expectedScript));
            Assert.That(idx, Is.EqualTo(expectedEndIdx));
        }

    }
}
