class BinaryTree:
    """
    We are implementing a binary tree in this module.
    """

    def __init__(self):
        # initialization here
        pass

    def pre_order(self):
        # root, left, right
        values = []

        def traversing(root):
            # Add value to list. Preorder is called on the full tree and traversing is called on the root node.

            if root == None:
                return
                #This means that we will just return if there is nothing in the node, we will just return or skip it. We do not need the if statements below when we have this return statement.

            values.append(root.value)

            # go left
            if root.left:
                traversing(root.left)

            # go right
            if root.right:
                traversing(root.right)

        traversing(self.root)

        return values

    def in_order(self):
        # Left, root, right


        values = []

        def traversing(root):
            # Add value to list. Preorder is called on the full tree and traversing is called on the root node.

            if root == None:
                return
                #This means that we will just return if there is nothing in the node, we will just return or skip it. We do not need the if statements below when we have this return statement.

            # go left
            if root.left:
                traversing(root.left)

            values.append(root.value)

            # go right
            if root.right:
                traversing(root.right)

        traversing(self.root)

        return values

    def post_order(self):
        # Left, right, root

        values = []

        def traversing(root):
            # Add value to list. Preorder is called on the full tree and traversing is called on the root node.

            if root == None:
                return
                #This means that we will just return if there is nothing in the node, we will just return or skip it. We do not need the if statements below when we have this return statement.

            # go left
            if root.left:
                traversing(root.left)

            # go right
            if root.right:
                traversing(root.right)

            values.append(root.value)

        traversing(self.root)

        return values


class Node:
    def __init__(self, value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node {self}"
