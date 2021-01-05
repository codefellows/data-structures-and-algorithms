class Node:
    """ Constructs Nodes with values and a reference to next for use with LinkedList
    
    Input <-- value: any, reference to next node
    Output --> object: node w/value and reference
    
    Time: O(1)
    Space: O(1)
    """ 
    def __init__(self, value: any, next= None):
        self.value = value
        self.next = next


class LinkedList:
    """builds an instance of a Singly Linked List. all relevant methods have their own docstrings

    Input <-- head, value: default='None'
    Output --> Object: instance='linked-list'

    Time: O(1)
    Space: O(1)
    """

    def __init__(self, head= None):
        # initialization here
        self.head = Node(head)
        

    def insert(self, value: any):
        """ adds a node to the begining of an instantiated linked list.

        Input <-- value: may be of any data type
        Output --> None

        Time: O(1)
        Space: O(N)
        """
        
        if self.head is not None:
            node = Node(value, self.head)
        self.head = node
    

    def includes(self, check: any) -> bool: 
        """ searches linked list for a value returns true if yes false if no. 
        Code based on psuedo code from reading asssingment @:https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html

        Input <-- value as check: may be of any type
        Output --> Boolean

        Time: O(N)
        Space O(1)
        """
        current = self.head
        
        while current:

            if current.value == check:
                return True
            else:
               current = current.next
                
        return False
        
    def __str__(self) -> str:
        """ prints string representation of entire instance of linked list, Node instances seperated by `->`

        Input <-- None
        Output --> str

        Time: O(N)
        Space: O(N)

        """
        once_and_future_string = ''
        current = self.head

        while current:
             
                once_and_future_string += f'{{ {current.value} }} -> '
                current = current.next

        return f'{once_and_future_string}None '        
        
       
               
    def append(self, value: any):
        """ adds the value passed as an argument to the end of the linked list. non-fruitful function. 

        input <-- int
        Output --> none (appends to list may be considered an implied return however)

        Space: O(1)
        Time: O(N)
        """
        current = self.head

        while current:
            if current.next == None:
                current.next = Node(value)
                return
            
            current = current.next

    
    def insert_before(self, val: any, new_val: any):
        """insert new_val before the val in a linked list Instance.

            Input <-- input1, input1 of any type
            Output --> mutates linked List instance

            Time: O(N)
            Space: O(N)
        """
        current = self.head
        if current.value == val:
            self.insert(new_val)
        else: #!!! explicit `else:` must be used. implied else raises AttributeError
            while current:
                if current.next.value == val:
                    node = Node(new_val, current.next) 
                    current.next = node
                    return

                current = current.next

    def insert_after(self, val: any, new_val: any):
        """insert new_val after val in an instance of LinkedList, if val does not exist appends new_val to the end of the lList instance

        Input <-- Input1, and input2 of any type
        Output --> mutates instance of LinkedList 

        Time: O(N)
        Space: O(N)
        """
        current = self.head
        
        while current:
            if current.value == val or None:
                node = Node(new_val, current.next)
                current.next = node
                break

            current = current.next


    def kth_from_end(self, k: int) -> any:
        """returns the value at the Kth position of an instance of LinkedList

            Input <-- Int
            Output --> any

            Time: O(N)
            Space: O(1)
        """
        try:
            spread = 0
            point = self.head
            rear_guard = None
            
            if not point:
                raise ValueError(f'cannot get {k}th value of an empty list')

            while point:
                if rear_guard:
                    point = point.next
                    rear_guard = rear_guard.next
                elif spread == k:
                    rear_guard = self.head
                else:
                    spread += 1
                    point = point.next
        
            return rear_guard.value
        except:
            return f'ValueError: {7} out of index range'
            
        # FIXME:  how do you test with assertion when using a built-in exception object??? it I don't seem to be able to even get to the test as the exception kills the program. 

        





        # current = self.head

        # if current == None:
        #     return f'an empty list has no Kth value, to use this method, first create a linked list'
        
        # counter = []

        # while current is not None:
        #     counter.append(current.value)
        #     current = current.next
        
        # if abs(k) > len(counter):
        #     return f'please enter a value less than {len(counter)}'
        
        # if k < 0:
        #     return counter[abs(k)]
        # else:
        #     return counter[len(counter)- k]


                
                    
                  

           



    











if __name__ == "__main__":
    finding_francis = LinkedList('goons')
    finding_francis.append('brown-pants')
    finding_francis.append('car-goon')
    print('pre-Insert_before',finding_francis.__str__())
    
    finding_francis.insert_before('brown-pants', 'meat-head')
    print('post-Insert_before', finding_francis.__str__())





   
    
    # finding_francis.insert_before('goons', 'meat-head')
    




# FIXME:  ASK ABOUT WHY THIS WASN'T WORKING: does current have access to the value of next without actually traversing to it?? 

#def insert_before(self, val, new_val):
        # node = Node(new_val)
        # current = self.head

        # if self.includes(val) == False:
        #     return f'the {val} you entered does not exist. to insert before this value, please add it to the LinkedList first'
        # else:
            
        #     while current is not None:
              
        #         if current.next == val:
      
        #             node.next = current.next
        #             current.next = node
        #             break

        #         current = current.next