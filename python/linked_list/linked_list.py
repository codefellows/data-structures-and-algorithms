class Node:
    """
    Creating a new node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None

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
    
    def insert_node(self, node):
        node.next = self.head
        self.head = node

    def search_node(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            else:
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
