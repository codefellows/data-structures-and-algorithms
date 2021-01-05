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
        """[Inserts a new node instanciation from Node class]

        Args:
            value ([int]): [the value we want our node to have]
        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def search_node(self, item):
        """[Search the linkedlist with the item(int) given]

        Args:
            item ([int]): [given this int if the current's value is equal to it then return True]

        Returns:
            [True/False]: [if the given int is in the linked list return true, if not return false]
        """
        current = self.head
        while current != None:
            if current.getvalue() == item:
                return True
            # else: else not needed
            current = current.getNext()
        return False

    def append(self, value):
        """[given a value, append this as a new node to the end of the linked list]

        Args:
            value ([int]): [an integer to be added as the value param of the node]
        """
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
        """[Given a value and a new_value, the value should be where we want to insert our new_value as a node before]

        Args:
            value ([int]): [we will find when the current.value is equal to this]
            new_value ([int]): [the new node that will be inserted to the linked list]
        """
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

        # Other way to do this

        # current = self.head
        # while current:
            # if current.value == value:
                # node = Node(new_val, current.next)
                # current.next = node
                # return
            # current = current.next
        
        # return "not in list"
    
    def insert_after(self, value, new_value):
        """[Give a value and new value we want to insert the new_value after the value when it's found in the linked list]

        Args:
            value ([int]): [find this value in the linked list]
            new_value ([type]): [the new node will be created with this and inserted to the linked list]
        """
        new_node = Node(new_value)
        current = self.head

        if current is None:
            self.insert_node(new_node)
            return
        
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            # return
    
    def kthFromEnd(self, k):
        """[Find the number given from the last of the linked list]

        Args:
            k ([int]): [the nth number from the last of the linked list]

        Returns:
            [int]: [where in the linked list, from the last, our k variable is]
        """
        current = self.head
        length = 0

        if k < 0:
            return 'Negative number has been entered'

        while current is not None:
            current = current.next
            length += 1

        if k > length:
            return 'Number is greater than the end of the list'

        current = self.head
        for num in range(0, length - k):
            current = current.next
        return current.value

        # Other way to do this

        # follower = None
        # pace_behind = 0
        # leader = self.head (goes till it hits none)

        # while leader: # while leader is not none
            # leader = leader.next # advance the leader
            # if follower: # if the follower is not none 
                # follower = follower.next
            # elif pace_behind == k: # Once the leader has reached the value k we move the follower
                # follower = self.head
            # else: # if no other conditions are met we increment
                # pace_behind += 1
        # if not follower:
            # raise ValueError("None")
        # return follower.value



        


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

if __name__ == '__main__':
    new_node = Node(1)
    link = LinkedList()
    link.insert_node(1)
    link.append(10)
    link.append(11)
    link.insert_after(11, 5)
    link.insert_node(3)
    print(link)
    