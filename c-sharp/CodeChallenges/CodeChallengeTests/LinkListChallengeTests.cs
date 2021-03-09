using System;
using Xunit;

using static LinkedLists.Program;

namespace CodeChallengeTests
{
  public class LinkListChallengeTests
  {
    [Fact]
    public void Test1()
    {
      bool itWorks = LinkListActivity();
      Assert.True(itWorks);
    }
  }
}
