# Blog Notes: Merge Sort

## Challenge

Write out an explanation of merge sort, walk through examples, and code it out. Also write unit tests to test your merge sort code.

## Merge Sort

Merge sort is a sorting mechanism that starts with taking in the elements in an array, breaking the array in half until you have one or two elements in consecutive order from the starting array, sorting these tiny pieces of the array, and then merging these pieces by halves until you are returned the full sorted array. While the array is being broken into pieces, it remains in the same order as it was input, it is not until the arrays are compared and merged that the numbers are sorted.

This can be very confusing to understand, A great visual of this sort method can be found [here](https://www.programiz.com/dsa/merge-sort). Merge sort is one of the slower sorting mechanisms (even slower than insertion sort) since it requires breaking things into pieces, comparing things, and putting things back together. It has an O(n*logn) time complexity and an O(n) space complexity as in the most divided state, all of the array elements would be separated and held in memory.

Let's look at some examples. In the code blocks the top set of numbers will be the broken out arrays and below that we will be counting the arrays for reference and clarity.

### Example 1

Say we were given the following regular array with numbers in the subsequent positions:

```
[8,4,23,42,16,15]
         1
```

We first break this array in half. Here we will assume that we always round up with our halves, so that if there are an odd number of elements, the first array would have more. numbers one(8) and two(4). They need to be swapped to put the array in order of least to greatest.

```
[8,4,23] [42,16,15]
     1       2
```

Then we will break these sub arrays in half as we defined it above where extra numbers default to the left array.

```
[8,4][23][42,16][15]
 1     2   3     4
```

Now that we have the original array broken into pieces with no more than two items, we will compare and sort the numbers insides of the mini arrays

```
[4,8][23][16,42][15]
 1     2   3     4
```

Now we will compare the arrays in pairs and merge them together in sorted order. Here we will merge array 1 with array 2, and merge array 3 with array 4

```
[4,8,23][15,16,42]
 1          2
```

Now we only have two arrays again. Again here, we will merge these two arrays into sorted order. Our final product will be one sorted array:

```
[4,8,15,16,23,42]
        1
 ```

### Example 2

Say we were given the following reversed array:

```
[20,18,12,8,5,-2]
        1
 ```

Again we would break this into pieces in half, sort the halves, and then return the sorted array following the same steps that are shown above in example 1. Lets break the array into halves until there are no more than two elements per mini array:
```
[20,18,12] [8,5,-2]
     1       2
```
```
[20,18][12][8,5][-2]
 1     2   3     4
```

Now that we have the original array broken into pieces with no more than two items, we will compare and sort the numbers insides of the mini arrays

```
[18,20][12][5,8][-2]
 1      2   3     4
```

Now we will compare the arrays in pairs and merge them together in sorted order. Here we will merge array 1 with array 2, and merge array 3 with array 4

```
[12,18,20][-2,5,8]
    1         2
```

Now we only have two arrays again. Again here, we will merge these two arrays into sorted order. Our final product will be one sorted array:

```
[-2,5,8,12,18,20]
        1
 ```


### Example 3

Say we are given a case where some of the values repeat:
```
[5,7,12,5,5,7]
      1
 ```

By achy breaky heart says we use this opportunity to break this array into mini arrays again. Let's do that.

```
[5,7,12] [5,5,7]
    1      2
```
```
[5,7][12][5,5][7]
 1     2   3   4
```
Lucky us, these broken out arrays are already sorted. So now let's merge arrays 1 and 2, and arrays 3 and 4.
```
[5,7,12][5,5,7]
     1     2
```

Then we will merge our last two arrays into their final order.

```
[5,5,5,7,7,12]
      1
```
### Example 4

Say we are given this nearly sorted array:

```
[2,3,5,7,13,11]
      1
 ```

The procedure is probably second nature conceptually at this point. Let's break up the given array:

```
[2,3,5][7,13,11]
    1     2
 ```

```
[2,3][5][7,13][11]
  1   2   3     4
 ```

Now let's sort and merge the pieces:

```
[2,3,5][7,11,13]
    1     2
 ```

```
[2,3,5,7,11,13]
      1
 ```

## Conclusions

According to [Geeks for Geeks](https://www.geeksforgeeks.org/quick-sort-vs-merge-sort/#:~:text=Merge%20sort%20is%20more%20efficient,larger%20array%20size%20or%20datasets.&text=Quick%20sort%20is%20more%20efficient,smaller%20array%20size%20or%20datasets.), there is a benefit to using merge sort over quick sort for larger datasets. While merge sort breaks every array into two parts so it can be done recursively, it seems like it would be faster to break the original dataset into n/2 parts from the beginning and then begin the sorting from there instead of taking the time to break the dataset into two over and over until we get arrays of one and two elements. In any event, it is interesting to look under the hood at how something like this comes together.

# Resources

See the code for the [Merge Sort](sorting/merge/merge_code.py) or the [Merge Sort Tests](sorting/merge/test_merge_code.py) by clicking on the highlighted words!

For more on markdown codeblock formatting, look [here](https://stackoverflow.com/questions/15721373/how-do-i-ensure-that-whitespace-is-preserved-in-markdown#:~:text=Use%20instead%20of%20space%20characters.)

Note to self - if you are having an import error for the tests:
- make sure there is an __init__.py file
- Make sure the folder name has UNDERSCORES and NOT dashes

To go back to the main ReadMe [Click Here](../../README.md)
