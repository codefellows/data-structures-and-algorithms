import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree, external_breadth

tree = BinaryTree()
tree.root = Node(2)
tree.root.left = Node(7)
tree.root.right = Node(5)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(11)
tree.root.right.right = Node(9)
tree.root.right.right.left = Node(4)

def test_breadth():
    actual = tree.breadth()
    expected = [2,7,5,2,6,9,5,11,4]
    assert actual == expected

def test_external_breadth():
    actual = external_breadth(tree)
    expected = [2,7,5,2,6,9,5,11,4]
    assert actual == expected