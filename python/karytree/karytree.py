from stack_and_queue.stacks_and_queues import Queue

class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def clone(self, converter=None):
        value = self.value

        if converter:
            value = converter(value)

        return Node(value)

class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self, converter=None):
        """
        return clone of self
        applies optional converter function to value of each node
        which is handy for things like fizz_buzz
        """

        clone_root = self.root.clone(converter)
        clone_tree = KaryTree(clone_root)

        pairs = Queue()

        pairs.enqueue((self.root, clone_root))

        while not pairs.is_empty():
            source_node, clone_node = pairs.dequeue()
            for source_child_node in source_node.children:
                clone_child_node = source_child_node.clone(converter)
                pair = (source_child_node, clone_child_node)
                pairs.enqueue(pair)
                clone_node.children.append(clone_child_node)
        return clone_tree