class Node:
    """
    Creating a new node class
    input: value for data and next.
    output: an instanciated node class with values for data and it's next.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class LinkedList:
    """
    Creates a linked list

    """
    def __init__(self):
        self.head = None
    
    def insert_node(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def search_node(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            # else: else not needed
                current = current.getNext()
        return False

    def __str__(self):
        temp = self.head
        node_list = [] 
        node_print = ''
        while(temp): 
            node_list.append(f"{ {temp.data} } -> ")
            temp = temp.next
            if temp == None:
              node_list.append('Null')
        for node in node_list:
          node_print += f'{node}'
        return node_print

        # Other way to do this
        # output = ''
        # current = self.head
        # while current is not None:
        #       output += f'{ {current.data} } -> '
        #       current = current.next
        # return output + 'Null'

        #################################################################
        #To-do for challenge 06
        # Create an append value, that adds a value to the end of the list

        # insert before(value, newVal) which will add a node with the given newValu before the first value node

        # insert after(value, newval) same as insert before but just after the value node.
