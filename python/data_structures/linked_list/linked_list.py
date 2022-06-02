class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():
    """
    This is the LinkedList Class
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    # This function currently makes a new node by calling the class node and passing in a value. Then it reassigns the new Node to the head of the Linked List.

    def traverse(self):
        # From class - want to use to test the insert function
        current = self.head
        while current:
            # This is saying while current is not none
            print(current.value)
            current = current.next

    def includes(self, value):
        # This function should indicate whether that value exists as a Node’s value somewhere within the list.
        # Should RETURN a Boolean
        current = self.head

        while current:
            if value == current.value:
                # Here we needed to tell the function to look at the VALUE of the item or node we are on.
                return True
            # End the loop if the answer is what you were looking for
            else:
                current = current.next
                # Go to the next item in the list if the item you were on was not the answer you are looking for
        else:
            return False
        # Apparently else works with while for an alternative to if the condition in the while loop is not met and the loop exhausts its paths.
        # This should return the other side of the boolean once current runs out of items in the list.

    def str(self):
        # This function should RETURN a string representing all the values in the Linked List
        # Self counts as no arguments because it is a method on its-SELF
        returned_string = ""
        current = self.head
        while current:
            returned_string += f"{ {current.value} } -> "
            current = current.next

        returned_string += "NULL"
        # returned_string.strip('\'') #!)@(*$@*#($#@*$@#(@)$(*#@($*#@))))
        return returned_string


if __name__ == '__main__':
    # ll = LinkedList()

    # brendon = Node(1)
    # brian = Node(2)
    # jae = Node(3)
    # jj = Node(4)
    # brendon.next = brian
    # brian.next = jae
    # jae.next = jj

    # ll.head = brendon

    # print(ll.includes(jae))
    # print(ll.includes('jae'))

    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")
    linked_list.traverse()
    # print(linked_list.includes("apple"))
    # print(linked_list.includes("apple"))
    # print(linked_list.includes("cucumber"))

    print(linked_list.str().strip('\''))
