# Merge Sort!

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## What is it?
Merge sort is a 'divide and conquer' style algorithm. It starts by finding the middle of the array/list, seperates the left and right, calls itself for the two halves, and then merges the two sorted halves. 

## Step through:

Start with declaring the mergesort function.

Declare your array's length in a variable. If the length variable is less than 1 then get your mid, left, right variables.

Left and right are based on the numbers before or after the mid in the array.

Recursively call the mergesort function on the left to then split the left side in the middle, it will continue to do this till there is only 1 value.

Recursively call the mergesort on the right till the same as above.

When the recursive functions if statement returns none then it runs the merge function.

Merge function takes in the left, right and array.

Start by declaring, i, j, and k variables set to 0.

Next begin a while loop with the condition, while i is less than the length of left variable and j is less than the length of right.

Check if the left array at position of i is less than or equal to right array at position j.

If that is true then array at position k is now equal to left at position i, add 1 to i and continue the while loop.

If that is not true then array at position k is now equal to right at position j, add 1 to j and continue the while loop.

either way always add 1 to variable k.

The final peice the algorithm checks if i is equal the length of left array, if that's true we set the remaining entries in arr to the remaining values in right.

If that isn't true then do the same thing but instead switch left for right.

