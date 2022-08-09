# Insertion Sort Code

def insertion_sort(test_array):
    """An in-place insertion-sort of an array - working"""
    # Make i the main pointer as you go through the array from the second item
    # Count from j to i where j starts at the first item
    # if i <= j
    # i goes to position j-1, j goes to 0, i gets deleted from its current position, test the new i
    for i in range (0,len(test_array)):
        for j in range (0,i):
            print(i,j)
            if test_array[i]<=test_array[j]:
                test_array.insert(j,test_array[i])
                del [test_array[i+1]]
                print(test_array)

    return test_array

def test_insertion_sort(test_array):
    """An in-place insertion-sort of an array"""
    for i in range (1,len(test_array)):
        for j in range(0,i):
            print(j,i)
            # print("outer",j,i,test_array)
            # if i == j:
            #     i +=1
            # if test_array[i] <= test_array[j]:
            #     # syntax is list.insert(position, element)
            #     print("helloinner1",j,i,test_array)
            #     test_array.insert(j,test_array[i])
            #     i+=1
            #     del [test_array[i]]
            #     print("inner2",j,i,test_array)
            # j=0
            # i=1
            # print("repeater",j,i,test_array)

    return test_array

def nearly_insertion_sort(test_array):
    # Works for all cases except reversed
    """An in-place insertion-sort of an array"""
    for i in range (1,len(test_array)):
        for j in range(0,i):
            print("outer",j,i,test_array)
            if i == j:
                i +=1
            if test_array[i] <= test_array[j]:
                # syntax is list.insert(position, element)
                print("helloinner1",j,i,test_array)
                test_array.insert(j,test_array[i])
                i+=1
                del [test_array[i]]
                print("inner2",j,i,test_array)
            # j=0
            # i=1
            # print("repeater",j,i,test_array)

    return test_array

def insertion_sort_with_notes(test_array):
    """An in-place insertion-sort of an array"""
    for i in range (1,len(test_array)):
        # i is looking at the second and further elements while j is looking at every element in the array to compare it to
        for j in range(0,len(test_array)-1):
            print("outer",j,i,test_array)
            # We are printing j first because it is the comparison and needs to keep restarting from the front of the array.
            if test_array[i] <= test_array[j]:
                # syntax is list.insert(position, element)
                print("helloinner1",j,i,test_array)
                test_array.insert(j,test_array[i])
                i+=1 # Advancing the outer count (aka going to the next variable for comparison) if we move a variable after comparing from the beginning of the array variable.
                del [test_array[i]]
                # Without this delete statement, the number would be inserted earlier into the array where it needed to go when sorted over and over and make an infinite loop and break. When you insert the value earlier you need to remove it from its current position.
                print("inner2",j,i,test_array)
    # There is probably an easier eay to do this using dictionaries.
    return test_array

# Version from class - This is making every value the largest value for some reason
def class_insertion_sort(test_array):
    for i in range(1,len(test_array)):
        j = i-1
        temp_number = test_array[i]
        print(j,i)
        while j>=0 and temp_number<test_array[j]:
            test_array[j+1] = test_array[j]
            j = j-1
        temp_number = test_array[j+1]
        print("hello", i, j)
    return test_array
