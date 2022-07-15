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

    def find_maximum_value(self):
        # Find the maximum value in an unorganized Binary Tree.
        #Using the preorder order of root, left, right.

        highest = self.root.value

        def traversing(root, highest):
            # Add value to list. Preorder is called on the full tree and traversing is called on the root node.

            if root == None:
                return
                #This means that we will just return if there is nothing in the node, we will just return or skip it. We do not need the if statements below when we have this return statement.


            current = root.value
            if current > highest:
                highest = root.value

            # go left
            if root.left:
                traversing(root.left, highest)

            # go right
            if root.right:
                traversing(root.right, highest)

        traversing(self.root, highest)

        return highest

    def find_maximum_value_list(self):
            # Find the maximum value in an unorganized Binary Tree.
            #Using the preorder order of root, left, right.

        highest = []

        def traversing(root):
            # Add value to list. Preorder is called on the full tree and traversing is called on the root node.

            if root == None:
                return
                #This means that we will just return if there is nothing in the node, we will just return or skip it. We do not need the if statements below when we have this return statement.

            highest.append(root.value)

            # if root.value > max:
            #     max = root.value

            # go left
            if root.left:
                traversing(root.left)

            # go right
            if root.right:
                traversing(root.right)

        traversing(self.root)

        return max(highest)

# O(h) space because the deepest thing is the depth of the callstack.
# O(N) time because we have to go through everything.

    def find_maximum_value_preorder(self):
            # Find the maximum value in an unorganized Binary Tree.
            #Using the preorder order of root, left, right.

        values_array = self.pre_order()
        #This gives you back the array of all items in the list
        highest = self.root.value
        #This is like setting to the first item in the values_array
        for number in values_array:
            if number > highest:
                highest = number

        return highest

class Node:
    def __init__(self, value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node {self}"
