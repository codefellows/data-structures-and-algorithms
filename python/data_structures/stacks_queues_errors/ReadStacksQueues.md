# Stacks and Queues Implementation

A challenge of creating classes for Nodes, Stacks and Queues

## Challenge

Implement push, pop, peak, and is_empty methods for stacks and enqueue, dequeue, peak and is_empty methods for queues.

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

dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

# Resources

TutorialsPoint shows that else can be used with while for the includes module.
https://ao.ms/convert-a-linkedlist-to-a-string-in-python/ (for help with what is described in the url)
https://favtutor.com/blogs/doubly-linked-list-python was used as a basis for doubly linked list code.

Worked with Brian, Aoife, Sergii, and Brendon to polish the enqueue function and pass the final test.
See the code for [Nodes](data_structures/node.py), [Stacks](data_structures/stack.py), and [Queues](data_structures/queue.py) by clicking on the highlighted words!
