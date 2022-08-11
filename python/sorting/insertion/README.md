# Blog Notes: Insertion Sort

## Challenge

Write out an explanation of insertion sort, walk through examples, and code it out. Also write unit tests to test your insertion sort code.

## Insertion Sort

Insertion sort is a sorting mechanism that starts by sorting the first two elements in an array. It then compares the third element with the first two and puts element three into the right place compared to elements one and two. From there, it continues through the array, comparing the current number to the sorted list of numbers before it before putting the current number in the right place compared to the previous numbers.

A great visual of this sort method can be found [here](https://www.toptal.com/developers/sorting-algorithms). Insertion sort is one of the slower sorting mechanisms since it requires comparing the current item to all of the items that came before it to put things into the correct place. Insertion sort is O(N) time complexity and O(1) space complexity when it is done in place.

### Example 1
Say we were given the following regular array with numbers in the subsequent positions:
```
[8,4,23,42,16,15]
 1 2 3  4  5  6
```
We first compare numbers one(8) and two(4). They need to be swapped to put the array in order of least to greatest.

```
[4,8,23,42,16,15]
 1 2 3  4  5  6
 ```

When we compare item three(23), and four(42), we find that they are in the correct places.

We would then look at item 5(16) and see that it needs to be moved to the third position as it is more than 8 but less than 23.

```
[4,8,16,23,42,15]
 1 2 3  4  5  6
```

Finally we would see that item 6 needs to be moved to being between items two(8) and three(16). When we make this final change, we would end up with the properly sorted array:

```
[4,8,15,16,23,42]
 1 2 3  4  5  6
 ```

### Example 2

Say we were given the following reversed array:

```
[20,18,12,8,5,-2]
 1  2  3  4 5  6
 ```

Essentially every iteration through the array, the current number would need to be moved to the beginning.

Step 1 - Moving Item 2:
```
[18,20,12,8,5,-2]
 1  2  3  4 5  6
 ```

Step 2 - Moving Item 3:
```
[12,18,20,8,5,-2]
 1  2  3  4 5  6
 ```

Step 3 - Moving Item 4:
```
[8,12,18,20,5,-2]
 1 2  3  4  5  6
 ```

Step 4 - Moving Item 5:
```
[5,8,12,18,20,-2]
 1 2  3  4  5  6
 ```

Step 5 - Moving Item 6:
```
[-2,5,8,12,18,20]
 1  2 3  4  5  6
 ```


### Example 3

Say we are given a case where some of the values repeat:
```
[5,12,7,5,5,7]
 1  2 3 4 5 6
 ```

This is a great place to consider using multiple pointers when doing a sorting mechanism. Essentially, as we look at each item in the array, we will start from the beginning of the array to look for a value that is more than or equal to the value we are looking at. When we find this more than or equal to value, we will drop the value in question before the comparing item.

When we first look at the above array, the first(5) and second(12) values are already in place. When we look at the third(7) value, this is when we need to move it into the second position.

```
[5,7,12,5,5,7]
 1  2 3 4 5 6
 ```

When we look at both the fourth(5) and fifth(5) positions, we notice that position one(5) is more than or **equal to** the value in question. Thus, the fourth and fifth 5's are technically put into the first position in each of their respective turns.

```
[5,5,7,12,5,7]
 4,1 2  3 5 6
 ```

```
[5,5,5,7,12,7]
 5 4 1 2  3 6
 ```

For clarity, now we change the index values based on where the values currently are.

```
[5,5,5,7,12,7]
 1 2 3 4  5 6
 ```

Since we already looked at the fifth value, the last one to look at is the sixth and last value. We see that the fourth(7) value is more than or **equal to** the sixth(7) value, so the sixth value is placed before the fourth value.

```
[5,5,5,7,7,12]
 1 2 3 6 4  5
 ```

Now we reassign the numbering and we have our sorted array.

```
[5,5,5,7,7,12]
 1 2 3 4 5 6
 ```

### Example 4

Say we are given this nearly sorted array:

```
[2,3,5,7,13,11]
 1 2 3 4  5  6
 ```

We go through the array and find that every item is in place according to the items before them except for one. We will make one swap between items 5(13) and 6(11) and this array will be sorted.

```
[2,3,5,7,11,13]
 1 2 3 4  5  6
 ```


## Resources

See the code for the [Insertion Sort](sorting/insertion/insertion_code.py) or the [Insertion Sort Tests](sorting/insertion/test_insertion_code.py) by clicking on the highlighted words!

[More on Pointers](https://thispointer.com/python-how-to-insert-an-element-at-specific-index-in-list/)

Note to self - if you are having an import error for the tests:

- make sure there is an __init__.py file
- Make sure the folder name has UNDERSCORES and NOT dashes

To go back to the main ReadMe [Click Here](../../README.md)
