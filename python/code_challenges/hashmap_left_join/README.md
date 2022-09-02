# Hashmap Left Join

A challenge of using Left Join for joining two hashmaps

## Approach & Efficiency

The Approach is to use two coded methods of Hashmaps. The first is the "keys" method that returns a list of all of the keys in the first hashmap. We will check if there is a matching key/value in the second hashmap for the key from the first hashmap. Then the key/value from the first hashmap and either the second hashmap value (or None) will be appended in a sublist of a list which will then be returned to the user. In the worst case this is O(N) for both time and O(N+M) space where N is the number of key/value pairs in the first hashmap and M is the number of matching key/value pairs in the second hashmap.

## API

The left_join function takes in the two hashmaps and returns a list of lists with the key, value from hashmap1, and value from hashmap2(if there is one).

## Resources

Worked with Aoife and Brian

## Whiteboard

For the Summary, Description, Approach & Efficiency, Solution, please see the whiteboard below:
![See my work here](/python/code_challenges/hashmap_left_join/Hashmap-Left-Join.png)

## Code

[See the Code](/code_challenges/hashmap_left_join/hashtable_left_join.py), [See the test file](code_challenges/hashmap_left_join/test_hashtable_left_join.py)

To go back to the main ReadMe [Click Here](../../README.md)
