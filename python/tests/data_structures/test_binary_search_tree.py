import pytest
from data_structures.binary_search_tree import BinarySearchTree


def test_exists():
    assert BinarySearchTree


@pytest.mark.skip("TODO")
def test_instantiate_empty():
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_to_empty():
    tree = BinarySearchTree()
    tree.add("apples")
    actual = tree.root.value
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_left():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    actual = tree.root.left.value
    expected = 5
    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_right():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    actual = tree.root.right.value
    expected = 15
    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_deeper(tree):
    tree.add(25)
    actual = tree.root.right.right.value
    expected = 25
    assert actual == expected


@pytest.mark.skip("TODO")
def test_contains(tree):
    actual = tree.contains(15)
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_contains_deeper(tree):
    actual = tree.contains(5)
    expected = True
    assert actual == expected


@pytest.mark.skip("TODO")
def test_not_contains(tree):
    actual = tree.contains(100)
    expected = False
    assert actual == expected


@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    return tree
