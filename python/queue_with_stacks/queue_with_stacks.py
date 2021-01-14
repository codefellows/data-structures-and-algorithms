from stack_and_queue.stacks_and_queues import Stack, Node, InvalidOperationError

####################################################################################
# Import not working so bringing this code over. Vince tried to help!!!
# class InvalidOperationError(BaseException):
#     pass

# class Node():
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# class Stack():
#     """
#     can only push items to the top and pop items from the top
#     FILO
#     """
#     def __init__(self, node=None):
#         self.top = node

  
#     def push(self, value):
#         # // INPUT <-- value to add, wrapped in Node internally
#         # // OUTPUT <-- none
#         node = Node(value)
#         node.next = self.top
#         self.top = node

#     def pop(self):
#         # // INPUT <-- self, for reference to top
#         # // OUTPUT <-- value of top Node in stack
#         # // EXCEPTION if stack is empty
#         if self.is_empty():
#             raise InvalidOperationError("Method not allowed on empty collection")
            
#         temp = self.top
#         self.top = self.top.next
#         temp.next = None
#         return temp.value
    
#     def peek(self):      
#         if self.is_empty():
#             raise InvalidOperationError("Method not allowed on empty collection")
#         return self.top.value

#     def is_empty(self):
#         # // INPUT <-- none
#         # // OUTPUT <-- boolean
#         if not self.top:
#             return True
#         else:
#             return False
####################################################################################


class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Args:
            value ([int]): [inserts the value to stack1 using FIFO]
        """
        self.stack1.push(value)

    def dequeue(self):
        """[Return the "first in" value from stack1.]

        Returns:
            [int/value]: [the first in value from stack1]
        """
        while self.stack1.peek():
            if self.stack1.top.next == None:
                return self.stack1.top.value
            else:
                temp = self.stack1.pop()
                self.stack2.push(temp)
                continue

if __name__ == '__main__':
    pq = PseudoQueue()
    #[10]->[15]->[20]
    pq.stack1.push(20)
    pq.stack1.push(15)
    pq.stack1.push(10)
    pq.enqueue(5)

    print(pq.stack1.top.value) # should be 5
    print(pq.stack1.peek())
    print(pq.dequeue())
    print(pq.stack2.top.value)
    # print(pq.stack2.top.next.value)
    # print(pq.stack2.top.next.next.value)
    