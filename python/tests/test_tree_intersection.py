import pytest
from tree_intersection.tree_intersection import tree_intersection
from tree.tree import BinaryTree, Node

@pytest.fixture()
def test_build_tree1():
    tree1 = BinaryTree()

    #tree1
    tree1.root = Node(150)
    #left
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    # right
    tree1.root.right = Node(250)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)
    return tree1

@pytest.fixture()
def test_build_tree2():
    tree2 = BinaryTree()

    #tree2
    tree2.root = Node(42)
    #left
    tree2.root.left = Node(100)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    # right
    tree2.root.right = Node(600)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.left = Node(4)
    tree2.root.right.right.right = Node(500)
    return tree2

@pytest.fixture()
def test_dupes_tree1():
    tree1 = BinaryTree()

    #tree1
    tree1.root = Node(1)
    #left
    tree1.root.left = Node(1)
    tree1.root.left.left = Node(5)
    tree1.root.left.right = Node(10)
    tree1.root.left.right.left = Node(5)
    # right
    tree1.root.right = Node(20)
    tree1.root.right.left = Node(2)
    tree1.root.right.right = Node(14)
    tree1.root.right.right.left = Node(2)
    tree1.root.right.right.right = Node(100)
    return tree1

@pytest.fixture()
def test_dupes_tree2():
    tree2 = BinaryTree()

    #tree2
    tree2.root = Node(1)
    #left
    tree2.root.left = Node(3)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(12)
    tree2.root.left.right.left = Node(15)
    # right
    tree2.root.right = Node(20)
    tree2.root.right.left = Node(23)
    tree2.root.right.right = Node(11)
    tree2.root.right.right.left = Node(2)
    tree2.root.right.right.right = Node(12)
    return tree2

def test_tree_intersection(test_build_tree1, test_build_tree2):
    actual = tree_intersection(test_build_tree1, test_build_tree2)
    expected = [100,125,160,175,200,350,500]
    assert actual == expected

def test_tree_intersection_dupes(test_dupes_tree1, test_dupes_tree2):
    actual = tree_intersection(test_dupes_tree1, test_dupes_tree2)
    expected = [1,2,20]
    assert actual == expected

def test_no_matches(test_build_tree1):
    no_match_tree = BinaryTree()
    no_match_tree.root = Node(400)
    actual = tree_intersection(test_build_tree1, no_match_tree)
    expected = 'None'
    assert actual == expected
