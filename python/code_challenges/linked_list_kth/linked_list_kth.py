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

    def __str__(self):
        # This function should RETURN a string representing all the values in the Linked List
        # Self counts as no arguments because it is a method on its-SELF
        # This is a string method  - like the dunder str and dunder repr from before (__str__)
        # This is the client facing string that shows if you just PRINT the class, no need to call with the dunder stuff.
        # The __repr__ is the dev facing piece. This is called with the repr dunder tags
        returned_string = ""
        current = self.head
        while current:
            returned_string += "{ " + current.value + " } -> "
            current = current.next

        returned_string += "Null"
        # None is the Null of python - you can update the test to match.
        # returned_string.strip('\'')
        return returned_string

    def append(self, new_value):
        current = self.head
        while current.next:
            current = current.next
            # This is to say if there is a current value we move to the next thing in the list
        else:
            new_node = Node(new_value)
            current.next = new_node

    def insert_before(self, old_value, new_value):
        current = self.head
        if self.includes(new_value):
            while current:
                if current.value == old_value:
                    self.insert(new_value )

                elif current.next.value == old_value:
                    new_node = Node(new_value, current.next)
                    current.next = new_node
                current.next = new_node

        # else: raiseTargetError

    def insert_after(self, old_value, new_value):
        current = self.head
        print(self, old_value, new_value)

        while current.value is old_value:
            # If we find our value in question as the next value
            new_node = Node(new_value)
            # Make a new node
            new_node.next = current.next
            # Set the new node next to the current current.next
            current.next = new_node
            # reset the current nodes next to the new node
            current = current.next
            # Move to the next node
        else:
            current = current.next

    def kth_from_end(self, k):
        length = 0
        current = self.head
        counter = 0
        while current:
            length += 1
            current = current.next
        if k > length:
            raise Exception
        else:
            counter = length - k
        current = self.head
        while counter-1:
            counter -= 1
            current = current.next
        return current.value

    def midpoint(self):
        length = 0
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
            print(current, counter)

        if counter <1:
            raise Exception
        else:
            counter = length//2
            # The double division sign is the floor division operator which rounds the quotient up to the nearest whole number

            length = 0
            current = self.head
            while length is not counter:
                while current:
                    length += 1
                    current = current.next


class TargetError(Exception):
    def __init__(self):
        self.message = "Error"

    def __str__(self):
        return self.message



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

    # linked_list = LinkedList()

    # linked_list.insert("apple")

    # linked_list.insert("banana")
    # linked_list.traverse()
    # # print(linked_list.includes("apple"))
    # # print(linked_list.includes("apple"))
    # # print(linked_list.includes("cucumber"))

    # print(linked_list)

    kth = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        kth.insert(value)
    print(kth.kth_from_end(0))
