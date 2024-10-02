using ConvertDict;
using Microsoft.VisualStudio.CodeCoverage;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject
{
    public class KeysConverterTest
    {
        private static char q = '"';

        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
            TestSingle("{Enter}", "{enter}");
        }

        [Test]
        public void Test2()
        {
            TestSingle("{Ctrl+v}", "{ctrl-v}");
        }

        [Test]
        public void Test3()
        {
            TestSingle("{Ctrl+Shift+Home}", "{ctrl-shift-home}");
        }

        [Test]
        public void Test4()
        {
            TestSingle("{Shift+ExtEnd}", "{shift-end}");
        }

        [Test]
        public void Test100()
        {
            Test("git branch -vv{Enter}", "git branch -vv{enter}");
        }

        [Test]
        public void Test101()
        {
            Test("{Ctrl+Shift+Home}git branch -vv{Enter}", "{ctrl-shift-home}git branch -vv{enter}");
        }

        private void Test(string ddKeys, string expectedTalonKeys)
        {
            string actual = KeysConverter.Convert(ddKeys);
            Assert.That(actual, Is.EqualTo(expectedTalonKeys));
        }

        private void TestSingle(string ddKeys, string expectedTalonKeys)
        {
            string actual = KeysConverter.ConvertSingleKey(ddKeys);
            Assert.That(actual, Is.EqualTo(expectedTalonKeys));
        }
    }
}
