# Blog Notes: Quick Sort

## Challenge

Write out an explanation of quick sort, walk through examples, and code it out. Also write unit tests to test your quick sort code.

## Quick Sort

Quick sort is a sorting mechanism where you choose a value in the array, and sort the rest of the array elements in relation to this element moving them to the left if the value is less and to the right of the pivot if its value is higher. Then pivot points are chosen for the sub arrays on either side of the pivot point and the subarrays are sorted consecutively again.

A great visual of this sort method can be found [here](https://favtutor.com/blogs/quick-sort-cpp). Quick sort can be unlucky when you choose a number that every number falls to one side of. For example, if you have the array [6,5,4,3,2,1] and your pivot is 5, essentially you still need to sort the front of the array. Quick sort works for smaller arrays like this since the data can have skewed pivot points such as in the previous example.

Let's look at some examples. For some reason, most examples use the last number as a pivot, but lets use the first number in the following examples.

### Example 1

Say we were given the following regular array with numbers in the subsequent positions:

```
[8,4,23,42,16,15]
```

Here, the first number, 8 is our pivot, so we sort based on whether the numbers are higher or lower than 8. We need to keep track of where the pivot point went because the pivot is the only item that we are sure is in the right position. Now er know where to split our array.

```
[4,8,23,42,16,15]
```

 Great, now our new pivot is the first number in the back half which is 23. Our new sorted array is:

```
[4,8,16,15,23,42]
```

Here we only need to sort what is essentially the middle section (numbers 15 and 16) with 16 as our pivot.

```
[4,8,15,16,23,42]
```

With that, we have our sorted array.

### Example 2

Say we were given the following reversed array:

```
[20,18,12,8,5,-2]
```

This is one of the cases where we have a skewed pivot. In every iteration, the pivot (the first item) will just get moved to the back which is visually demonstrated like so:

```
[18,12,8,5,-2,20]
```
```
[12,8,5,-2,18,20]
```
```
[8,5,-2,12,18,20]
```
```
[5,-2,8,12,18,20]
```
```
[-2,5,8,12,18,20]
```
Sorted!

### Example 3

Say we are given a case where some of the values repeat. The second lines here refer to the reference position of the numbers in the array:
```
[5,7,12,5,5,7]
 1 2 3  4 5 6
 ```

Here we can define that values less than or **equal to** our pivot will be moved to the left.

```
[5,5,5,7,12,7]
 4 5 1 2 3  6
```
Here the two fives that were in positions 4 and 5 get moved to being before the 5 that was in position 1. Let's reset our count and pivot again.

```
[5,5,5,7,12,7]
 1 2 3  4 5 6
 ```
Now we will pivot around the 7 in position 4.
```
[5,5,5,7,7,12]
 1 2 3 6 4 5
 ```

Now the 7 from position 6 is put before the 7 in position 4 and our array is sorted.

### Example 4

Say we are given this nearly sorted array:

```
[2,3,5,7,13,11]
 ```

This is another example where our pivot is skewed.

```
[2,3,5,7,13,11]
 1 2 3 4  5  6
 ```

We go through the array use the pivots for array indexes 1(2),2(3),3(4) and 4(7) and find no change. Finally, when we use index 5(13) as the pivot, index 5(13) and index 6(11) are swapped. returning the sorted array.

```
[2,3,5,7,11,13]
 1 2 3 4  5  6
 ```

## Conclusion

This works best with a random, relatively small, and evenly distributed set of numbers. This works in O(n log n) time.

## Resources

Here are two resources with pseudo code or code in Python and C++ that this code is based on.

One explanation of quicksort with a great visual can be found [here](https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/tutorial/)

See another example of quicksort implementation and the basis for this code [here](https://www.programiz.com/dsa/quick-sort)

See the code for the [Quick Sort](sorting/quick/quick_code.py) or the [Quick Sort Tests](sorting/quick/test_quick_code.py) by clicking on the highlighted words!

Note to self - if you are having an import error for the tests:
- make sure there is an __init__.py file
- Make sure the folder name has UNDERSCORES and NOT dashes

To go back to the main ReadMe [Click Here](../../README.md)
