from msilib.schema import Error


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList():
    """
    This is the LinkedList Class
    """
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node
    #This function currently makes a new node by calling the class node and passing in a value. Then it reassigns the new Node to the head of the Linked List.

    def includes(self, value):
        #This function should indicate whether that value exists as a Node’s value somewhere within the list.
        #Should RETURN a Boolean
        current = self.head
        while current:
            if value == current:
                return True
            #End the loop if the answer is what you were looking for
            else:
                current = current.next
                #Go to the next item in the list if the item you were on was not the answer you are looking for
        else:
            return False
        #Apparently else works with while for an alternative to if the condition in the while loop is not met and the loop exhausts its paths.
        #This should return the other side of the boolean once current runs out of items in the list.


    def str(list):
        #This function should RETURN a string representing all the values in the Linked List
        returned_string = ""
        current = list.head
        while current:
            returned_string += "{  } -> ".format(list.value)
            current = current.next
            return returned_string

        else:
            returned_string += "NULL"


# class TargetError:
#     try:
#         print ('Jae')
#     except Error as e:
#         print('That\'s the name of your dev!')


if __name__ == '__main__':
    ll = LinkedList()

    brendon = Node(1)
    brian = Node(2)
    jae = Node(3)
    jj = Node(4)
    brendon.next = brian
    brian.next = jae
    jae.next = jj

    ll.head = brendon

    ll.includes(jae)
    #I could not get an answer back from the program when I ran this as a script sooo no idea if the includes function is even working.
