def first_repeated_word(passage):

    if type(passage)!= str:
        print("Please enter a valid string")

    if len(passage) <2:
        return None

    passage = passage.lower()
    words_list= passage.split(" ")

    # Remember split needs to be set as an array, it does this directly
    hashtable = Hashtable()

    for word in words_list:

        if hashtable.contains(word) == True:
            return word

        else:
            hashtable.set(word, 0)
    return None


class Hashtable:
# Need to add the hashtable to this folder/file when you get it working.
    def __init__(self, size = 3):
        # Change the size back to 1024 when you're done.
        # We are taking the list and filling the values with None in every index to begin with. We are giving the list the length of 10224 to begin with.
        self.size = size
        self._buckets = size * [None]

    def contains(self, key):
        print(key)

    def set(self, key):
        print(key)
