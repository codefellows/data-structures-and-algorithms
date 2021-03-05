
# Recursive solution with an internal helper method. 

# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length
      # ^^  assign length of array to a variable     
#     if n > 1
      # ^^  check for length greater than 1 element 
#       DECLARE mid <-- n/2
      # ^^ assign the middle of arr to a variable
#       DECLARE left <-- arr[0...mid]
      # ^^ assign left side of arr to a variable
#       DECLARE right <-- arr[mid...n]
      # ^^ assign right side of arr to a variable
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
    # ^^ assigns first of 3 index counters tracks left arr index
#     DECLARE j <-- 0
    # ^^ assigns second of 3 index counters tracks right arr index
#     DECLARE k <-- 0
    # ^^ assgins third of 3 index counters  tracks whole arr index

#     while i < left.length && j < right.length
    # as long as first index less than len(leftarr) AND j lessthan len(rightarr)
#         if left[i] <= right[j]
        # ^^ compare both sides at correlative index
#             arr[k] <-- left[i]
        # ^^ re-assign arr[k] to the value of left[i]
#             i <-- i + 1
        # ^^ increment i
#         else
#             arr[k] <-- right[j]
        # ^^ assign arr[k] to the value of right[j]
#             j <-- j + 1
        # ^^ increment j
#         k <-- k + 1
        # ^^ always increment k

#     if i = left.length
    # ^^ check length of left 
#        set remaining entries in arr to remaining values in right
#     else
#        set remaining entries in arr to remaining values in left

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[0 : mid]
        right = arr[mid : n -1]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # if i == len(left):
    #     arr.extend(right)
    # else:
    #     arr.extend(left)