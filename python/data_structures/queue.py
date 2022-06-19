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

        # Why is it that we do not need to set the next of the front to the first rear for this to work? Based on the way this is currently it seems like the front would be detached from the rest of the queue

        # else:
            # if self.rear is None:
            #     self.rear = node
            #     self.front.next = self.rear
            #     #If there is just one item in the queue (front) then its next is the rear
            # elif self.rear is not None:
            #     self.rear.next = node
            #     #If there is a rear value then we are setting its next to this new value.


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
