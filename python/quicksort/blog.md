# QuickSort Algorithm

Writen by, Anthony Beaver

## What is it??

You guessed it, another divide and conquer algorithm used to sort a given array. This specific style uses pivot points and partitions.

### The step through

We define a function named quicksort that takes an array, a left (the first index of our array), and right (the last index of our array).

Within the function check if the length of the array is equal to 1, if its then we have nothing left to do, return the array.

Otherwise, "if" the left is less than the right do the following:

Declare a variable ("p"), store the return of a function we will create later called 'partition'.

The next two steps are to call our quicksort function recursively.

- First recursive function takes the original array, the left and the partitionn variable subtracted by 1

- Second recursive function takes the original array, the partitionn plus 1 and the right.

The final step within the quicksort function is to return the array.

> Lets take a step back and create the partitician function.

Define a function named partitionn that takes an array, the "low" and the "high" variables.

First thing you must do is declare a variable, let's call it 'i', 'i' will equal the low variable subtracted by 1.

Declare a 'pivot' variable that will equal the array at position of 'high'.

Start a for loop based on the range from 'low' to 'high' with a variable of 'j' to iterate.

"If" the array at position of 'j' is less than or equal to the pivot variable, then we add one to 'i' and we call a function called swap (we will build this next).

Outside our loop we do a bit of reassigning:
- array at position i plus 1 will equal array at position 'high'
- array at position 'high' will equal array at position i plus 1

This will move our array forward for another comparision.

We are still in the partitionn variable and we must return something. We now return variable i plus 1

> Let's now create our swap function

Define a function named swap. Swap will take an array, and 2 different variables('i' and 'j').

Start with creating a variable named 'temp', 'temp' will equal array at position 'i'.

Now we reassign array at position of 'i' to array at position 'j'.

Final reassignment, array at position 'j' will now equal the 'temp' variable.

### Conclusion

The last thing to do is test. 

When quicksort is given the array of [8, 4, 23, 42, 16, 15], left being equal to 0, and making sure to assign the 'right' variable to the length of array - 1 our function should return:[4, 8, 15, 16, 23, 42].

This blog was writen with the python language in mind but can be translated to other programming languages.