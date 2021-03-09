using System;
using System.Collections.Generic;

namespace DataStructures
{
  class Program
  {
    static void Main(string[] args)
    {
      LinkedListFun();
    }

    static void LinkedListFun()
    {
      LinkedList<int> myNumbers = new LinkedList<int>(1);
      myNumbers.Insert(2);
      myNumbers.Insert(3);
      myNumbers.Insert(4);
      myNumbers.Insert(5);
      myNumbers.Insert(6);
      myNumbers.Insert(7);
      myNumbers.Insert(8);
      myNumbers.Print();
    }

  }
}
