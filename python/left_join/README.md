<!-- Challenge 05 -->
# LEFT JOIN
<!-- Short summary or background information -->

    Write a function that LEFT JOINs two hashmaps into a single data structure.
    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
    LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
    The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
    Avoid utilizing any of the library methods available to your language.


## Challenge
<!-- Description of the challenge -->
To find any keys from the left that match with the right and store both values in a data struct. Return the data struct

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I want to use dictionaries for this, seperate the dictionaries and compare the keys. Then store that in a list and return it.

## Solution
<!-- Embedded whiteboard image -->
[Link to whiteboard image](../assets/left_join.PNG)
