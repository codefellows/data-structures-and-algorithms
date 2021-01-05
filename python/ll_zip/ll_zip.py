class Node:
    """
    Creating a new node class
    input: value for value and next.
    output: an instanciated node class with values for data and it's next.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Creates a linked list

    """
    def __init__(self, head=None):
        self.head = head
    
    def insert_node(self, value):
        """[Inserts a new node instanciation from Node class]

        Args:
            value ([int]): [the value we want our node to have]
        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def __str__(self):
        output = ''
        current = self.head
        while current is not None:
              output += f'{{ {current.value} }} -> '
              current = current.next
        return output + 'NULL'

def zipLists(list1, list2):
    link = LinkedList()
    # head = Node(0)
    # # ptr = head
    l1 = list1.head
    l2 = list2.head

    while True:
        if l1 is None and l2 is None:
            break
        else:
            next_val = 0
            # print(l1.value)
            # get the first val from l1
            next_val = l1.value
            print(next_val)
            l1 = l1.next
            # add it to our new linked list
            link.insert_node(next_val)
            # ptr.next = next_val
            # ptr = ptr.next

            print(l2.value)
            next_val = l2.value
            link.insert_node(next_val)
            l2 = l2.next
            # ptr.next = newNode
            # ptr = ptr.next
    return link


if __name__ == '__main__':
    # new_node = Node()
    link = LinkedList()
    link.insert_node(5)
    link.insert_node(3)
    link.insert_node(1)
    link2 = LinkedList()
    link2.insert_node(6)
    link2.insert_node(4)
    link2.insert_node(2)
    #print(link, link2)
    zipped = zipLists(link, link2)
    print(zipped)

    