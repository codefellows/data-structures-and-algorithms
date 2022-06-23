from .stack import Stack
from .invalid_operation_error import InvalidOperationError

class PseudoQueue():
    """
    The pseudo-queue class where we will use stacks to mimic queues.
    """

    def __init__(self, value=None, next=None):
        self.original = Stack()
        self.new = Stack()
        self.value = value
        self.next = next
        #Whenever we make a new PseudoQueue we will make these new stacks.

    def dequeue(self):
        """Arguments: none
    Returns: the value from node from the bottom of the original stack
    Takes all of the elements, puts them into a new or temporary stack, pops out the new top value (which was the bottom of the stack or the front of the queue), transfers all elements from the new stack to the original stack.
    """
        if self.original is not None:

            while self.original.is_empty is False:
                transition = self.original.pop()
                self.new.push(transition)
            bottom_rung = self.new.pop()
            while self.new.is_empty is False:
                status_quo = self.new.pop()
                self.original.push(status_quo)
            return bottom_rung

        else:
            raise InvalidOperationError

    def enqueue(self, value):
        """Arguments: value
    Returns: The Updated Stack
    Adds the node to the top of the stack which here is the nack of the queue.
    """
        self.original.push(value)
        # This works because original is the name here for the Stack of its values
        return self.original



if __name__=="__main__":
    pass
