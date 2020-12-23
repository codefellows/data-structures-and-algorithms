class Node:
    """
    Creating a new node class
    input: value for value and next.
    output: an instanciated node class with values for data and it's next.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def getvalue(self):
        return self.value

    def getNext(self):
        return self.next

class LinkedList:
    """
    Creates a linked list

    """
    def __init__(self, head=None):
        self.head = head
    
    def insert_node(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def search_node(self, item):
        current = self.head
        while current != None:
            if current.getvalue() == item:
                return True
            # else: else not needed
            current = current.getNext()
        return False

    def append(self, value):
        new_node = Node(value)
        current = self.head

        #check for empty list
        if current is None:
            self.insert_node(new_node)
            return
        while current.next is not None:
            current = current.next

        current.next = new_node
        return

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        current = self.head

        if current is None:
            self.insert_node(new_node)
            return
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            return

    def __str__(self):
        # temp = self.head
        # node_list = [] 
        # node_print = ''
        # while(temp): 
        #     node_list.append(f"{ {temp.value} } -> ")
        #     temp = temp.next
        #     if temp == None:
        #       node_list.append('Null')
        # for node in node_list:
        #   node_print += f'{node}'
        # return node_print

        # Other way to do this
        output = ''
        current = self.head
        while current is not None:
              output += f'{{ {current.value} }} -> '
              current = current.next
        return output + 'NULL'

        #################################################################
        #To-do for challenge 06
        # Create an append value, that adds a value to the end of the list

        # insert before(value, newVal) which will add a node with the given newValu before the first value node

        # insert after(value, newval) same as insert before but just after the value node.

# if __name__ == '__main__':
#     new_node = Node(1)
#     link = LinkedList()
#     link.insert_node(1)
#     link.append(10)
#     print(link)
    