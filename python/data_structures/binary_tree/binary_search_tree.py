from .binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    This class builds on a binary tree to create a binary search tree. This assumes that you cannot add values that already exist in the tree. Look at how it is written - this is saying BinarySearchTree extends BinaryTree
    """

    def __init__(self):
        # This is so that even if a tree is empty, it will have some root node.
        self.root = None

    def add(self, value):

        node = Node(value)
        #Wrapping the given value into a node.

        if self.root is None:
            self.root = node
            return

        def binary_traverse(root, node):
            if not root:
                return
            #Is the value we are trying to insert larger or smaller than the root?


            if node.value<root.value:
                if root.left:
                    binary_traverse(root.left, node)
                else:
                    root.left = node

            else:
                if root.right:
                    binary_traverse(root.right, node)
                else:
                    root.right = node

        binary_traverse(self.root, node)

    def contains(self, value):
        # This is the cleaned version of what you were trying to do below.
        boolean_value = []

        def contains_traverse(root, value):
            if not root:
                return

            if root.value == value:
                boolean_value.append(True)

            if value<root.value:
                if root.left:
                    contains_traverse(root.left, value)

            else:
                if root.right:
                    contains_traverse(root.right, value)

        contains_traverse(self.root, value)

        return len(boolean_value) == 1

    def contains_messy(self, value):
        # Do this by traversing the binary search tree not passing things into a linked list
        boolean_value = []

        def contains_traverse(root, value):
            if not root:
                # boolean_value = False
                return

            if root.value == value:
                boolean_value.append(True)

            if value<root.value:
                if root.left:
                    contains_traverse(root.left, value)
                # else:
                #     boolean_value = False

            else:
                if root.right:
                    contains_traverse(root.right, value)
                # else:
                #     boolean_value = False

        contains_traverse(self.root, value)

        return len(boolean_value) == 1
        #This did not like the true or false values. It was thinking the boolean value was set to None, and was NOT waiting until the full traversal of the table before returning an answer to the function. In a recursive function


    def other_contains(self,value):
        current = self.root
        while current:
            if current.value == value:
                return True
            if value<current.value:
                if current.left:
                    current = current.left
                else:
                    break

            else:
                if current.right:
                    current = current.right
                else:
                    break
        return False
