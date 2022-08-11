# Merge Sort Code

import math

def merge_sort(test_array):
    """Uses recursion for comparison for the merge sort feature. Based on Class Pseudocode."""

    if (type(test_array) is not list):
        # This is for the edge case where not a list is passed in.
        print("You need to input a list into this function")
        return

    length = len(test_array)

    if length <2 :
        return test_array
        #If the array is empty or there is only one item in the array

    if length>1:
        half = math.ceil(length/2)
        left = test_array[0:half]
        right = test_array[half:length]
        # Surprisingly this sorts out the numbering between the left and right arrays.

        merge_sort(left)
        merge_sort(right)

        zipped_array = comparison_merge_reintegrate(left,right,test_array)

        print("zipped = ", zipped_array)
        return zipped_array


def comparison_merge_reintegrate(left,right,given_array):
    i = 0
    j = 0
    k = 0

    while (i<len(left)) and (j<len(right)):
        # if there are values in BOTH the left and right array - compare and zipper merge into sorted order
        if left[i] <=right[j]:
            given_array[k] = (left[i])
            i += 1
            # Another way to do this would be to ditch the counter and pop these from the array
            print("1")
        else:
            given_array[k] = (right[j])
            j += 1
            print("2")

        # print("3")
        k +=1
        print("left =", left,"right =", right, "full =", given_array," i = ", i, "j =", j, "k =", k)

    # if only one side has values left, put them in at the end. For the 2&1 situations.
    if (i<len(left)):
        # If there are values only in the left array left over
        given_array[k:] = (left[i:])
        print("leftover left")

            # This takes the elements from i to the end of the array.
    elif (j<len(right)+1):
        # If there are only values in the right array left over
        given_array[k:] = (right[j:])
        print("leftover right")


    print("final given =", given_array)
    return given_array



