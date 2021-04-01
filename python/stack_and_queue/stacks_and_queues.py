class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack():
    """
    can only push items to the top and pop items from the top
    FILO
    """
    def __init__(self, node=None):
        self.top = node

  
    def push(self, value):
        # // INPUT <-- value to add, wrapped in Node internally
        # // OUTPUT <-- none
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        # // INPUT <-- self, for reference to top
        # // OUTPUT <-- value of top Node in stack
        # // EXCEPTION if stack is empty
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
            
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
    
    def peek(self):      
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        # // INPUT <-- none
        # // OUTPUT <-- boolean
        if self.top == None:
            return True
        else:
            return False

class Queue():

    """
    FIFO
    LILO
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # // INPUT <-- value to add to queue (will be wrapped in Node internally)
        # // OUTPUT <-- none
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node #<-- node
            self.rear = node #<-- node

    def dequeue(self):
        # // INPUT <-- none
        # // OUTPUT <-- value of the removed Node
        # // EXCEPTION if queue is empt 
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        temp = self.front
        self.front = self.front.next
        # temp.next = None
        return temp.value

    def is_empty(self):
        # // INPUT <-- none
        # // OUTPUT <-- boolean
        if self.front == None:
            return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        # return top's value
        return self.front.value