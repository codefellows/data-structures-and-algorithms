using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructures
{
  public class LinkedList<T>
  {

    public Node<T> Head { get; set; }


    /// <summary>
    /// Plain, Empty Linked LList
    /// Head will be null
    /// Usage: LinkedList myList = new LinkedList();
    /// </summary>
    public LinkedList() { }

    /// <summary>
    /// Linked list constructor that creats a head node
    /// Usage: LinkedList myList = new LinkedList(5);
    /// </summary>
    /// <param name="value"></param>
    public LinkedList(T value)
    {
      Node<T> node = new Node<T>(value);
      Head = node;

    }

    public void Insert(T value)
    {
      Node<T> node = new Node<T>(value);
      node.Next = Head;
      Head = node;
    }

    public void Append(T value)
    {
    }

    public void Remove(Node<T> node)
    {
    }

    public void Print()
    {
          Node<T> current = Head;

          while (current != null)
          {
            Console.Write($"[{current.Value}] => ");
            current = current.Next;
          }

          Console.WriteLine("NULL");
    }


  }
}
