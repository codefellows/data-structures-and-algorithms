from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1000):
        self.size = size
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0

        for ch in key:
            sum += ord(ch)
        primed = sum * 3
        index = primed % self.size
        return index
    
    def set(self, key, value):
        #hashed index key
        h_i_key = self._hash(key)

        # Find out if the bucket is empty, if it is create a ll, otherwise add to the ll.
        if not self._buckets[h_i_key]:
            self._buckets[h_i_key] = LinkedList()
        
        self._buckets[h_i_key].insert_node((key, value))
    
    def get(self, requested_key):
        #hash the key
        h_key = self._hash(requested_key)

        temp = self._buckets[h_key]

        if temp is None:
            return None
        else:
            current = temp.head

            while current is not None:
                if current.value[0] == requested_key:
                    return current.value[1]
            
                current = current.next
            return None

    def contains(self, requested_key):
        #hash the key
        h_key = self._hash(requested_key)

        temp = self._buckets[h_key]

        if temp.head is None:
            return False
        else:
            current = temp.head

            while current is not None:
                if current.value[0] == requested_key:
                    return True
            
                current = current.next
            return False

