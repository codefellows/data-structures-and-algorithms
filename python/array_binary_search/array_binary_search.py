# Iteratively

list1 = [4,8,15,16,23,42]
key1 = 15
list2 = [11,22,33,44,55,66,77]
key2 = 90

# Iterative with a for loop
def BinarySearch(list, key):
    first = 0
    last = len(list)-1
    index = -1
    for i in range(first, last):
        # print(i)
        if key == list[i]:
            index = i
    else:
        return index

print(f'list 2: {BinarySearch(list2, key2)}')

# Binary with a while loop
def BinarySearchWhile(list, key):
    first = 0
    last = len(list)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if list[mid] == key:
            index = mid
        else:
            if key<list[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(f'Binary search While: {BinarySearchWhile(list1, key1)}')