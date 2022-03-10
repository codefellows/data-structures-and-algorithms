import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_exists():
    assert BinaryTree


@pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = []
    tree.pre_order(actual.append)
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = []
    tree.in_order(actual.append)
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = []
    tree.post_order(actual.append)
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree
