# Hashmap Tree Intersection

A challenge of finding shared values between two binary trees.

## Approach & Efficiency

The Approach is to map every word from the first tree into a hashmap with a key from the number of the leaf. If numbers are repeated in the first tree, we ignore them. Then we do a lookup of the numbers from the second tree with the keys that were assigned to the hasnmap (the numbers from tree 1). If the number from the second tree exists in the hashmap, we add it to a list. We finally run the list through a set and back to make sure there are no duplicates from numbers that are repeated in the second tree.

## API

The tree_intersection function is where the code from the above approach is stored.

## Resources



## Whiteboard

For the Summary, Description, Approach & Efficiency, Solution, please see the whiteboard below:
![See my work here](/python/code_challenges/tree_intersection/Hash-Tree-Repeaters.png)

## Code

[See the Code](code_challenges/tree_intersection/tree_intersection.py), [See the test file](code_challenges/tree_intersection/test_tree_intersection.py)

To go back to the main ReadMe [Click Here](../../README.md)
