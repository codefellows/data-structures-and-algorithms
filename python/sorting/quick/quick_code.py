# Quick Sort Code

def quick_sort(test_array):
    """Prepare the arrays going in to be sorted"""
    left = 0
    right = len(test_array)-1
    return actual_sort(test_array,left,right)

def actual_sort(test_array,left,right):
    """QuickSort function with the pivot as the first item"""
    # Left and right are indicies of items in the test_array.

    if left<right:
        starter_pivot = swap(test_array,left,right)

        #Sort the left the the right sides
        actual_sort(test_array,left,starter_pivot-1)
        actual_sort(test_array,starter_pivot+1,right)

    return test_array
    #This is the sorted version since things are sorted in place.

def swap(starter_array, left_index,right_index):
    """This should be moving the elements less than the pivot element to the left in the array, leaving the greater items in the right, and returning the position of the pivot."""
    pivot_index = starter_array[left_index]
    temp_index = left_index+1
    for i in range ((left_index+1),right_index):
        print("0",starter_array[i],pivot_index)
        if starter_array[i]<pivot_index:
            #swap the lower item and the pivot item positions- remember you can reassign two things on one line
            print("1",pivot_index,starter_array[i], starter_array[temp_index])
            (starter_array[i],starter_array[temp_index]) = (starter_array[temp_index],starter_array[i])
            temp_index += 1
            print("2",starter_array[i], starter_array[temp_index])

    print("3",starter_array[left_index],starter_array[temp_index])
    (starter_array[left_index], starter_array[temp_index-1]) = (starter_array[temp_index-1], starter_array[left_index])
    print("4",starter_array[left_index],starter_array[temp_index])
    print(temp_index-1)
    return temp_index-1

    # We are not getting into the if statement at all currently.
