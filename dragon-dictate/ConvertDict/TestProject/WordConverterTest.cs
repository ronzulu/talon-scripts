using ConvertDict;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject
{
    public class WordConverterTest
    {
        [Test]
        public void Test001()
        {
            Test(5, "five");
        }

        [Test]
        public void Test002()
        {
            Test(15, "fifteen");
        }

        [Test]
        public void Test003()
        {
            Test(20, "twenty");
        }

        [Test]
        public void Test004()
        {
            Test(27, "twenty seven");
        }

        [Test]
        public void Test005()
        {
            Test(100, "one hundred");
        }

        [Test]
        public void Test006()
        {
            Test(155, "one hundred fifty five");
        }

        [Test]
        public void Test007()
        {
            Test(305, "three hundred [zero] five");
        }

        [Test]
        public void Test008()
        {
            Test(2024, "twenty [hundred] twenty four");
        }

        public void Test(int v, string expectedStr)
        {
            string word = "[" + v.ToString() + "]";
            string? actual = WordConverter.ConvertDragonWordToTalonRule(word);
            Assert.That(actual, Is.EqualTo(expectedStr));
        }
    }
}
