# Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
  
    # PreOrder method
    def pre_order(self):
        pre_order_list = []
        def traverse(root):
            if not root:
                return
            pre_order_list.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return pre_order_list

    # In order method
    def in_order(self):
        in_order_list = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            in_order_list.append(root.value)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return in_order_list

    # In post order
    def post_order(self):
        post_list = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            post_list.append(root.value)
        traverse(self.root)
        return post_list

    def find_maximum_value(self):
        val = 0
        check = self.pre_order()
        for i in check:
            if val < i:
                val = i
        return val

        ### Second method
        # def traverse(root):
        #     nonlocal val
        #     val = root.value
        #     if not root.right and not root.left:
        #         return
        #     if root.left:
        #         if val < root.left.value:
        #             traverse(root.left)
        #         else:
        #             traverse(root.right)
        #     else:
        #         traverse(root.right)
        # traverse(self.root)
        # return val

    def breadth(self):
        root = self.root

        if root is None:
            return
        
        to_print = []
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            to_print.append(queue[0].value)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)

        return to_print
       
# Create a BinarySearchTree class

class BinarySearchTree(BinaryTree):
# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
    def __init__(self, root = None):
        super().__init__(root)

    def add(self, val):
        def insert(root, val):
            if root is None:
                return Node(val)
            else:
                if root.value == val:
                    return root
                elif root.value < val:
                    root.right = insert(root.right, val)
                else:
                    root.left = insert(root.left, val)
            return root
        insert(self.root, val)

# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
    @staticmethod
    def contains(root, val):
        if root.value == val:
            return True
        elif root.value < val:
            if root.right == None:
                return False
            else:
                return BinarySearchTree.contains(root.right, val)
        else:
            if root.left == None:
                return False
            else:
                return BinarySearchTree.contains(root.left, val)


def external_breadth(tree):
    root = tree.root

    if root is None:
        return
    
    to_print = []
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        to_print.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)

    return to_print


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    # tree.root = Node(50)
    # tree.root.left = Node(30)
    # tree.root.right = Node(70)
    # tree.root.left.left = Node(20)
    # tree.root.left.right = Node(40)
    # tree.root.right.right = Node(80)
    # tree.add(60)
    # print(tree.pre_order())
    print(external_breadth(tree))
    # print(tree.contains(tree.root, 34))

