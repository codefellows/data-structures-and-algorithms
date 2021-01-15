class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter():
    """
    FIFO
    LILO
    """
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        # // INPUT <-- value to add to queue (will be wrapped in Node internally)
        # // OUTPUT <-- none
        low_val = value.lower()
        # if low_val != 'dog' and low_val != 'cat':
        #     low_val = 'null'
        
        node = Node(low_val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node 
            self.last = node 

    def dequeue(self, perf):
        low_perf = perf.lower()
        if low_perf != 'dog' and low_perf != 'cat':
            low_perf = 'null'
        # // INPUT <-- none
        # // OUTPUT <-- perfue of the removed Node
        # // EXCEPTION if queue is empt 
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        temp = self.first
        while temp.value != low_perf:
            if low_perf != 'dog' and low_perf != 'cat':
                temp.value = 'null'
                return temp.value
            elif low_perf != 'dog':
                temp = self.first.next
                continue
            elif low_perf != 'cat':
                temp = self.first.next
                continue
        
        self.first = self.first.next
        temp.next = None

        

        return temp.value

    def is_empty(self):
        # // INPUT <-- none
        # // OUTPUT <-- boolean
        if self.first == None:
            return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        # return top's value
        return self.first.value

if __name__ == '__main__':
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("Lizard")
    print(a.dequeue('cat'))