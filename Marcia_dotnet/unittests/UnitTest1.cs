using System;
using Xunit;

namespace unittests
{
    public class UnitTest1
    {
        [Fact]
        public void TestarIdade()
        {
            Pessoa p = new Pessoa();
            bool r = p.Idade(20);
            Assert.IsTrue(r, "Testado");
        }
    }
}
