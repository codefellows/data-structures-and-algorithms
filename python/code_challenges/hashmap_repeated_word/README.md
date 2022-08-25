# Hashmap Repeated Word

A challenge of finding the first repeated word in a passage using a hashmap.

## Approach & Efficiency

The Approach is to map every word from the passage into a hashmap as a key with the value being a counter. When a word-key is already in the hashmap as a key, we will return that word as the same word that repeats. In the worst case this is O(N) for both time and space where n is the number of words in the passage.

## API

The repeated_word function initializes the hashmap, and stores words as indicies using methods from the Hashmap class.

## Resources

Splitting Strings <https://appdividend.com/2022/05/30/how-to-split-string-with-multiple-delimiters-in-python/#:~:text=To%20split%20a%20string%20with%20multiple%20delimiters%20in%20Python%2C%20use,each%20occurrence%20of%20the%20pattern.>
String Lengths <https://www.w3schools.com/python/gloss_python_string_length.asp#:~:text=To%20get%20the%20length%20of,use%20the%20len()%20function.>

## Whiteboard

For the Summary, Description, Approach & Efficiency, Solution, please see the whiteboard below:
![See my work here](/python/code_challenges/hashmap_repeated_word/Hashmap_Repeated_Words.png)

## Code

[See the Code](/code_challenges/hashmap_repeated_word/hashtable_repeated_word.py), [See the test file](code_challenges/hashmap_repeated_word/test_hashtable_repeated_word.py)

To go back to the main ReadMe [Click Here](../../README.md)
