from .kary_tree import KaryTree, Node
#The issue is that python saves things with equals as new references.


def fizz_buzz_trees(kary1):
    kary2 = KaryTree()

    def traversing(root):
        if root == None:
            return
        print(root.value)

        kary2.root = Node(fizz_buzz(root.value))

        # root.value = fizz_buzz(root.value)

        if root.children:
            for child in root.children:
                traversing(child)


    traversing(kary1.root)

    # print(kary1.breadth_first())
    # print(kary2.breadth_first())
    # print(kary1, kary2)
    return kary2

def fizz_buzz_tree_start_3_passes(kary1):
    kary2 = KaryTree()
    kary2.root = fizz_buzz(kary1.root.value)
    return kary2

def fizz_buzz_trees(kary1):
    """We are cloning the original tree and then traversing it rewriting its values with the fizzbuzz function."""
    kary2 = KaryTree()

    # kary2 = kary1
    # We start with cloning the tree, and do a preorder traversal passing the values through and modifying them in place for kary2

    def traversing(root):
        if root == None:
            return

        root.value = fizz_buzz(root.value)

        if root.children:
            for child in root.children:
                traversing(child)


    traversing(kary2.root)

    # print(kary1.breadth_first())
    # print(kary1, kary2)
    return kary2

def fizz_buzz_tree_passes_2(kary1):
    """We are cloning the original tree and then traversing it rewriting its values with the fizzbuzz function."""
    kary2 = kary1
    # We start with cloning the tree, and do a preorder traversal passing the values through and modifying them in place for kary2

    def traversing(root):
        if root == None:
            return

        root.value = fizz_buzz(root.value)
        print(root.value)

        if root.children:
            for child in root.children:
                traversing(child)


    traversing(kary2.root)

    # print(kary1.breadth_first())
    # print(kary1, kary2)
    return kary2

def fizz_buzz(value):
    """FizzBuzz written separately for testing and clarity."""
    new_value = ""
    if value%3==0 and value % 5==0:
        new_value = "FizzBuzz"
        # print(new_value)
        return new_value
    elif value%3==0 and value % 5 !=0:
        new_value = "Fizz"
        # print(new_value)
        return new_value
    elif value%5 ==0 and value % 3!=0:
        new_value = "Buzz"
        # print(new_value)
        return new_value
    else:
        new_value = str(value)
        # print(new_value)
        return new_value



# Traverse all the way down the tree. Change the numbers to fizzBuzz and set the collection as the children to the previous node in the new tree.


def fizz_buzz_tree_thinking(kary1):
    """Original thought process had us using the kary queue and that is not needed. We can accomplish what we are looking for by traversing the kary tree. """


    kary2 = kary1
    # We start with cloning the tree, and do a preorder traversal passing the values through and modifying them in place for kary2

    def traversing(root):
        if root == None:
            return

        root.value = fizz_buzz(root.value)

        if root.children:
            for child in root.children:
                traversing(child)


    traversing(kary2.root)

    print(kary2)

    # length = len(kary1.root.children)


    # for i in range (length):
    #     kary2.root.children[i] = fizz_buzz(kary1.root.children[i])

    # queue = Queue()
    # queue.enqueue(kary1.root)

    # while not queue.is_empty():
    #     node = queue.dequeue()

    #     new_value = fizz_buzz(node.value)
    #     #It seems that we should link the children back to kary2 here
    #     new_node = Node(new_value)
    #     for child in node.children:
    #         queue.enqueue(child)

    return kary2
