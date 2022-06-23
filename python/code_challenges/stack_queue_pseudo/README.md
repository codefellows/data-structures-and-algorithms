# Stacks and Queues Implementation

## Challenge

Implement a queue using two stacks

## API

Method Explanations:
push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

peek
Arguments: none
Returns: Value of the node located at the top of the stack or the front of the queue
Should raise exception when called on empty stack

is_empty
Arguments: none
Returns: Boolean indicating whether or not the stack or queue is empty.

enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

In this case we are putting the new argument into the bottom of the stack.

dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

In this case it should pop the item on top of the stack.

Note - if the folders are named with dashes then the import statements will just not work. Note for self. Names of folders need to be in snake case.

# Resources

See the whiteboard ![Here!](/python/code_challenges/stack-queue-pseudo/CC11.png)


See the code for [The Pseudo Queue](/code_challenges/stack-queue-pseudo/stack_queue_pseudo.py), or the [Tests](/code_challenges/stack-queue-pseudo/test_stack_queue_pseudo.py) by clicking on the highlighted words!

To go back to the main ReadMe [Click Here](../../README.md)
