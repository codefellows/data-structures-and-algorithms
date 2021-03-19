# Write a function called tree_intersection that takes two binary tree parameters.
# Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

from tree.tree import BinaryTree

def tree_intersection(bt1, bt2):
    # convert the binary trees to arrays
    arr1 = bt1.in_order()
    arr2 = bt2.in_order()

    # place to store the matches
    matches = []

    # loop through
    for i in range(len(arr1)):
        # if any instance of arr1 is in arr2 then...
        if arr1[i] in arr2:
            # if arr1 at that instance is already in matches then skip it.
            if arr1[i] in matches:
                continue
            # if it's in arr2 and it's not already in matches then store it in matches.
            else:
                matches.append(arr1[i])
    if matches == []:
        return 'None'
    return matches

