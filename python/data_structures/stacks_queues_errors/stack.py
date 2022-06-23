from .node import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Stack Class
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        """Arguments: value
        Adds a new node with that value to the top of the stack with an O(1) Time performance."""
        node = Node(value)
        if self.top is not None:
            node.next = self.top
        self.top = node

    def pop(self):
        """Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack"""
        if self.top:
            top_value = self.top.value
            self.top = self.top.next
            return top_value
        else:
            raise InvalidOperationError

    def peek(self):
        """Arguments: none
        Returns: Value of the node located at the top of the stack or the front of the queue
        Should raise exception when called on empty stack"""

        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        """Arguments: none
        Returns: Boolean indicating whether or not the stack or queue is empty. If it is empty it is true."""
        if self.top:
            return False
        else:
            return True
