from .binary_tree import BinaryTree
from .queue import Queue
from .invalid_operation_error import InvalidOperationError


def breadth_first(tree):

    tree_queue = Queue()
    tree_list = []

    try:
        if not tree.root:
            pass
        else:
            tree_queue.enqueue(tree.root)
            while tree_queue.front:
                if front_node.left:
                    tree_queue.enqueue(front_node.left)
                if front_node.right:
                    tree_queue.enqueue(front_node.right)
                front_node = tree_queue.dequeue(tree_queue.front)
                tree_list.append(front_node.value)
        return tree_list

    except:
        raise InvalidOperationError
