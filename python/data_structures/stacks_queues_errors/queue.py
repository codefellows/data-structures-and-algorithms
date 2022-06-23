from .node import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    The queue class
    """

    def __init__(self, front=None, rear = None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        """Arguments: value
        Adds a new node with that value to the rear of the queue with an O(1) Time performance."""
        node = Node(value)
        if self.front is None:
            self.front = node
            #If there are no items in the list the first is the front.
        if self.rear:
            self.rear.next = node


        self.rear = node
            #This runs in either case
            #If we are putting something into the list line 22 is setting something to the front and to the rear. Look at the spacing. This happens in both cases and runs outside of the second if statement.
            # Not every if needs an else in python.

        # Why is it that we do not need to set the next of the front to the first rear for this to work? Based on the way this is currently it seems like the front would be detached from the rest of the queue
        # The last line is setting whatever we put into the stack as the rear. Thus is there is only one item going in it will be both the front and the rear.


    def dequeue(self):
        """Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue"""
        if self.front:
            front_value = self.front.value
            self.front = self.front.next
            return front_value
        else:
            raise InvalidOperationError

    def peek(self):
        """Arguments: none
        Returns: Value of the node located at the top of the stack or the front of the queue
        Should raise exception when called on empty stack"""
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        """Arguments: none
        Returns: Boolean indicating whether or not the stack or queue is empty."""
        if self.front == None:
            # print(self.front, self.rear)
            return True
        # else:
        #     return False
