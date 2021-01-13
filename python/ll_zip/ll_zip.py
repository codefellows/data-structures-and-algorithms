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
   
    def append(self, value):
        """[given a value, append this as a new node to the end of the linked list]

        Args:
            value ([int]): [an integer to be added as the value param of the node]
        """
        new_node = Node(value)
        current = self.head

        #check for empty list
        if current is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next

        current.next = new_node
        return

    def __str__(self):
        output = ''
        current = self.head
        while current is not None:
              output += f'{{ {current.value} }} -> '
              current = current.next
        return output + 'NULL'

def zipLists(list1, list2):
    link = LinkedList()

    l1 = list1.head
    l2 = list2.head

    while True:
        if l1 is None and l2 is None:
            break
        else:
            next_val = 0
            next_val = l1.value
            #print(next_val)
            l1 = l1.next
            link.append(next_val)

            #print(l2.value)
            next_val = l2.value
            link.append(next_val)
            l2 = l2.next

    return link
    """
    other way to do this:
    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        l1_next = l1.next
        l2_next = l2.next

        l1.next = current_ll2

        #check for l1_next, if none then break
        if not l1_next:
            break

        l2.next = l1_next

        # now store the next, nexts
        l1, l2 = l1_next, l2_next
        or
        l1 = l1_next
        l2 = l2_next

        return l1

    """


if __name__ == '__main__':
    # new_node = Node()
    link = LinkedList()
    link.append(1)
    link.append(3)
    link.append(5)
    link2 = LinkedList()
    link2.append(2)
    link2.append(4)
    link2.append(6)
    # print(link)
    # print(link2)
    zipped = zipLists(link, link2)
    print(zipped)

    