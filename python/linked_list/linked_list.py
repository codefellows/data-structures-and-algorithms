class LinkedList:
    """
    builds an instance of a Singly Linked List. all relevant methods have their own docstrings

    Input <-- head, value: default='None'
    Output --> Object: instance='linked-list'

    Time: O(1)
    Space: O(1)
    """

    def __init__(self, value=None):
        # initialization here
        self.head = Node(value)
        

    def insert(self, value):
        """ adds a node to the begining of an instantiated linked list.
        Input <-- value: may be of any data type
        Output --> None

        Time: O(1)
        Space: O(N)
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node
    
    def includes(self, check):
        """ searches linked list for a value returns true if yes false if no. 
        Code based on psuedo code from reading asssingment @:https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html

        Input <-- value as check: may be of any type
        Output --> Boolean

        Time: O(N)
        Space O(1)
        """
        current = self.head
        
        while current is not None:

            if current.value == check:
                return True
            else:
               current = current.next
                
        return False
        
    def __str__(self):
        """ prints string representation of entire instance of linked list, Node instances seperated by `->`

        Input <-- None
        Output --> str

        Time: O(N)
        Space: O(N)

        """
        once_and_future_string = []

        current = self.head

        while current is not None:
             
                once_and_future_string.append(f'{{ {current.value} }} ->')
                current = current.next
                
                
        once_and_future_string.append('None ')        
        console_log = ' '.join(once_and_future_string)
        return console_log
               
            
                

class Node:
    """ Constructs Nodes with values and a reference to next for use with LinkedList
    
    Input <-- value: any, reference to next node
    Output --> object: node w/value and reference
    
    """ 
    def __init__(self, value, next=None):
        self.value = value
        self.next = next





if __name__ == "__main__":
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')
    finding_francis.insert('car-goon')

    finding_francis.includes('goons')
    