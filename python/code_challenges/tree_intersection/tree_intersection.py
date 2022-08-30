from .binary_tree import BinaryTree
from .hashtable import Hashtable

def tree_intersection(tree1, tree2):
    repeaters_list = []
    if tree1 or tree2 do not have a node:
        return repeaters_list

    hashmap = Hashmap()

    for node in tree1:
        in-order traverse tree1
        true_false = hashmap.get(node.value)
        if true_false is False:
            hashmap.set(node.value)

    for node in tree2:
        in-order traverse tree2
        comparison = hashmap.get(node.value)
        if comparison is True:
            repeaters_list.append(node.value)

    set(repeaters_list)
    list(repeaters_list)

    return repeaters_list
