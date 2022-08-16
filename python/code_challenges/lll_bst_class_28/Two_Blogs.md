# A Tale of Two Blog Topics

## Linked List Largest Value and Binary Search Tree Largest Value Walkthroughs

### Linked List Largest Value Walkthrough

A singly linked list is a data structure with items called nodes that store two sets of information - their value and the location of the next node if there is one. For more information on how linked lists work see [here](https://realpython.com/linked-lists-python/). When we move through a linked list we can only see the value of the current node, and in a singly linked list, we cannot see any previous values. This is called a traversal.

Say we are given a linked list with the following values:

```
5 -> 2 -> 9 -> 7 -> 4 -> None(End)
```

Since we can see all of the information, or the linked list values, we can easily see that 10 is the greatest number in this linked list. But let's say that each of these numbers was on a different planet and the portal between planets wiped your mind. How would we keep track of the values then?

When we code, we can store information in variables outside of our current operation. Let's go further into our imagination and say that we are allowed a magical etch-a-sketch in our teleportation journey that could store one number and would not get wiped between planets. If we are looking for the maximum number on any of the planets, we can write a number on the etch-a-sketch at the first planet, and then compare the number we have with the planet's number on the subsequent planets. If the new planet has a greater number, we erase the number previously on the etch-a-sketch and write down the new number. The highest number we write on the etch-a-sketch will be the last number we have written down by the time we leave. For the previously written linked list, let's take another look while keeping track of the highest number we have seen so far:

```
5 -> 2 -> 9 -> 7 -> 4 -> None(End)
5    5    9    9    9    Winner: 9
```

To write this in pseudo-code:

```
function spacemission(linkedList):
  etch-a-sketch-value = 0
  traverse(linkedList):
    for every value in the linked list:
      check if the value is higher than the etch-a-sketch-value
        if it is:
          update the etch a sketch value with the current value
      move to the next value in the linked list
    return the etch-a-sketch-value
```


### Binary Search Tree Largest Value Walkthrough

A binary search tree (BST) is a data structure filled with numbers that are sorted in a particular order. Some number is chosen to be the root or the top number, and all number to the left of the root are less than the root, and all numbers to the right of the root are more than the root. To learn more about the BST data structure check it out [here](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

Say we have the following BST:

```
         5
      /     \
    2         8
  /   \     /   \
1      4   7     9
```

If I asked you to do this as a person, you would soon find the highest value is 9. But how did we do this? Since we know that the highest value is always on the right, we glued our eyes to the right of the tree and followed the values all the way down.

It is almost like finding our way out of a maze by keeping our hand only on the right wall. Like the etch a sketch example though, it would be helpful if we kept some sort of track of the highest number we have seen so far.

How would we tell a computer to do this? When we go value by value through a BST we can call it traversing too. Let's go through this maze with our etch-a-sketch again.

```
function maze(BST):
  etch-a-sketch-value = 0
  root = BST-root-value

  function traverse(node):
    etch-a-sketch-value = current-node-value
    if node-has-a-right:
      traverse(to the right)

  if the tree has a root:
    traverse(root)

  return the etch-a-sketch-value
```

This is a bit different than the previous example, but what do we have going on here? Essentially, we have a traverse function (written inside of the maze function) that is keeping our hand on that right wall of the maze. When we call the inner traverse function, we save the value we currently have and check if this value has anything to the right. Counterintuitively, the second part of the function starts us off at the top of the tree.

Let's step through our original BST to see if we can follow along.

```
         5
      /     \
    2         8
  /   \     /   \
1      4   7     9
```

The computer reads through the function from the top. It registers the inner traverse function but sees no reason to look further into it yet. But hey, we hit an if statement: Is there a root here? Yes it is 5. So we will call the traverse function we passed by earlier and save 5 into the etch-a-sketch.

The next question is does 5 have anything to its right? Why, yes it does, there is an 8.

So now we save 8 to the etch-a-sketch and check again - does 8 have anything to its right? Again, our answer is yes, we get to the value of 9 which we save into our etch-a-sketch.

Here something different happens. There is no further value to the right of 9. We break out of the loop like a daydream. Good thing we had our etch-a-sketch keeping track of the highest value. When we check it, there is a 9 which is the highest value from the BST. Another successful mission.


To go back to the main ReadMe [Click Here](../../README.md)
