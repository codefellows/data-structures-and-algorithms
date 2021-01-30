import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree

def test_instantiate_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_single_root():
    tree = BinaryTree()
    tree.root = Node(1)
    actual = tree.root.value
    expected = 1
    assert actual == expected

def test_add_right_and_left():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(3)
    tree.root.right = Node(15)
    actual = f"{tree.root.value}, {tree.root.left.value}, {tree.root.right.value}"
    expected = "10, 3, 15"
    assert actual == expected

def test_preorder():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(30)
    tree.root.right = Node(70)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(40)
    actual = tree.pre_order()
    expected = [50, 30, 20, 40, 70]
    assert actual == expected

def test_inorder():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(30)
    tree.root.right = Node(70)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(40)
    actual = tree.in_order()
    expected = [20, 30, 40, 50, 70]
    assert actual == expected

def test_postorder():
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(30)
    tree.root.right = Node(70)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(40)
    actual = tree.post_order()
    expected = [20, 40, 30, 70, 50]
    assert actual == expected