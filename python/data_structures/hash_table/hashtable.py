class Hashtable:
    """
    Several functions that can be used for a Hashtable implementation. The Key refers to the string that you would like to add to the hash table.
    """

    #Sanitize the input to make sure that you have a string. ie. turn numbers into strings.
    # We need to write/import linked list and node for this.
    # If you are adding to an index, does something exist at the index or not?
    # If there is nothing at the index? Need to create a new linked list at that index

    def __init__(self, size = 3):
        # Change the size back to 1024 when you're done.
        # We are taking the list and filling the values with None in every index to begin with. We are giving the list the length of 10224 to begin with.
        self.size = size
        self._buckets = size * [None]

    def hash(self,key):
        """Argument: key - which is the input string
        Returns: Index in the collection for that key somewhere between 0 and one less that the size of the list.
        Convert each item in the given array using the ord() method.
        Total the ord() method values amd multiply by a larger prime number to induce more randomness into the conversion
        Take the modulus of the total as compared to the length of the hash table
        Return the number of the index"""

        sum = 0

        for character in key:
            sum += ord(character)

        primed = sum*23

        index = primed % self.size

        return index

    def set(self,key,value):
        """Adds an item to the hash table"""
        """ Arguments: key, value
        Returns: nothing
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        if key is None:
            return

        key = str(key)

        index = self.hash(key)

        linked = LinkedList()

        if self._buckets[index] is None:
            linked.insert(value)
            # The insert function handles making the new value the head if a value is there and adding a value if nothing is there.


    def get(self,key):
        """Returns the head of anything at this value in the linked list. """
        """Arguments: key
        Returns: Value associated with that key in the table"""
        index = self.hash(key)
        value = self._buckets[index]
        return value

    def contains(self,key):
        """Argument: Key
        Returns: Boolean, indicating if anything is in the bucket/ key exists in the hash table already."""
        # Is there anything at this index? Is it the key sent in? If not is the next thing that value?

    def keys(self,key):
        """Argument: key
        returns: Collection of keys at all indices, aka the whole hash table.Return all of the keys where the value is not none. It is an index before any value is assigned, a key when a value is assigned."""







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

        returned_string += "None"
        # None is the Null of python - you can update the test to match.
        # returned_string.strip('\'')
        return returned_string










