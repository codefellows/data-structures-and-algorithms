######
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

    
######

def FizzBuzzTree(tree):
    # root = tree.breadth()
    # new_tree = BinaryTree()
    # return_tree = BinarySearchTree(new_tree)
    # if root is None:
    #     return
    
    # return_arg = []
    # for i in root:
    #     if (i % 3 == 0) and (i % 5 == 0):
    #         val = 'FizzBuzz'
    #         return_arg.append(val)
    #     elif (i % 5 == 0):
    #         val = 'Buzz'
    #         return_arg.append(val)
    #     elif (i % 3 == 0):
    #         val = 'Fizz'
    #         return_arg.append(val)
    #     else:
    #         i_str = str(i)
    #         return_arg.append(i_str)
    # for j in return_arg:
    #     return_tree.add(j)
    # return return_tree
    
    
    
    # return_array = []
    # queue = []
    # queue.append(root)
    # print(queue[0].value)
    # while(len(queue) > 0):
    #     f_b = queue.pop(0)
    #     print(f_b)
    #     if (root.value % 3 == 0) and (root.value % 5 == 0):
    #         f_b = Node('FizzBuzz')
    #         if root.left is not None:
    #             f_b.left = root.left
    #             queue.append(root.left)
    #         if root.right is not None:
    #             f_b.right = root.right
    #             queue.append(root.right)
    #         print(f_b.value)
    #         # return_tree.root = f_b
    #         return_array.append(f_b)
    #     elif root.value % 5 == 0:
    #         f_b = Node('Buzz')
    #         if root.left is not None:
    #             f_b.left = root.left
    #             queue.append(root.left)
    #         if root.right is not None:
    #             f_b.right = root.right
    #             queue.append(root.right)
    #         # return_tree.root = f_b
    #         return_array.append(f_b)
    #     elif root.value % 3 == 0:
    #         f_b = Node('Fizz')
    #         if root.left is not None:
    #             f_b.left = root.left
    #             queue.append(root.left)
    #         if root.right is not None:
    #             f_b.right = root.right
    #             queue.append(root.right)
    #         # return_tree.root = f_b
    #         return_array.append(f_b)
    #     else:
    #         # return_tree.root = root
    #         return_array.append(f_b)
    #         queue.append(root.left)
    #         queue.append(root.right)
    # return return_array


    return_tree = BinaryTree()
    root = tree.root

    def traverse(root):
  
        if not root:
            return
        print('traverse root value is:', root.value)
        if (root.value % 3 == 0 and root.value % 5 == 0):
            f_b = Node('FizzBuzz')
            f_b.left = root.left
            f_b.right = root.right
            return_tree.root = f_b
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 5 == 0:
            buzz = Node('Buzz')
            buzz.left = root.left
            buzz.right = root.right
            return_tree.root = buzz
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 3 == 0:
            temp = root
            fizz = Node('Fizz')
            fizz.left = root.left
            fizz.right = root.right
            return_tree.root = fizz
            traverse_left(temp.left)
            traverse_right(temp.right)
        else:
            return_tree.root = root
            traverse_left(root.left)
            traverse_right(root.right)
    # return
    

    def traverse_left(root):
        if not root:
            return

        print("traverse left root val:", root.value)
        if (root.value % 3 == 0 and root.value % 5 == 0):
            print("left value fizzbuzz is:", root.value)
            f_b = Node('FizzBuzz')
            f_b.left = root.left
            f_b.right = root.right
            return_tree.root.left = f_b
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 5 == 0:
            buzz = Node('Buzz')
            buzz.left = root.left
            buzz.right = root.right
            return_tree.root.left = buzz
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 3 == 0:
            fizz = Node('Fizz')
            fizz.left = root.left
            fizz.right = root.right
            return_tree.root.left = fizz
            traverse_left(root.left)
            traverse_right(root.right)
        else:
            return_tree.root.left = root
            traverse_left(root.left)
            traverse_right(root.right)
    # traverse_left(root)
        # return

    def traverse_right(root):
        if not root:
            return
        print("traverse right root val:", root.value)
        if (root.value % 3 == 0 and root.value % 5 == 0):
            f_b = Node('FizzBuzz')
            f_b.left = root.left
            f_b.right = root.right
            root.right = f_b
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 5 == 0:
            buzz = Node('Buzz')
            buzz.left = root.left
            buzz.right = root.right
            return_tree.root.right = buzz
            traverse_left(root.left)
            traverse_right(root.right)
        elif root.value % 3 == 0:
            fizz = Node('Fizz')
            fizz.left = root.left
            fizz.right = root.right
            return_tree.root.right = fizz
            traverse_left(root.left)
            traverse_right(root.right)
        else:
            return_tree.root.right = root
            traverse_left(root.left)
            traverse_right(root.right)
        # traverse_right(root)
    traverse(root)
    

    return return_tree

if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(6)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(10)
    tree.root.right = Node(7)
    tree.root.right.left = Node(15)


    new_tree = FizzBuzzTree(tree)

    print('new tree root is:', new_tree.root.value)
    print('new tree root left is:', new_tree.root.left.value)
    print(new_tree.root.right.value)
    print('new tree root left.left is:',new_tree.root.left.left.value)
    print(new_tree.root.left.right.value)
    print(new_tree.root.right.left.value)
    