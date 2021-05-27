# 2D Array 
<!-- Short summary or background information -->
Given a 6x6 2d Array, there are 16 hourglasses.

Hourglass example:
```
1 0 0
  2 
1 1 1
```

## Challenge
<!-- Description of the challenge -->
Return the maximum sum out of all 16 hourglasses.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
A nested for loop is my approach. The reason is because we need to loop through the 6x6, grabbing the first list's 3, the next list only grabs the middle( position 1 to start) then we need to get the third list's 3. Repeate this but add 1 to each iteration so it will move the hourglass.