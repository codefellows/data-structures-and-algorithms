import pytest
from data_structures.binary_tree import BinaryTree, Node
from code_challenges.tree_breadth_first import breadth_first


def test_exists():
    assert breadth_first


@pytest.mark.skip("TODO")
def test_none_tree():
    expected = []
    actual = breadth_first(None)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_rootless_tree():
    tree = BinaryTree()
    expected = []
    actual = breadth_first(tree)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_single_node():
    tree = BinaryTree()
    tree.add("apples")
    expected = ["apples"]
    actual = breadth_first(tree)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_two_nodes():
    tree = BinaryTree()
    tree.add("apples")
    tree.add("bananas")
    assert tree._root.value == "apples"
    assert tree._root.left.value == "bananas"


@pytest.mark.skip("TODO")
def test_two_nodes():
    tree = BinaryTree()
    tree.add("apples")
    tree.add("bananas")
    expected = ["apples", "bananas"]
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_four_nodes():
    tree = BinaryTree()
    tree.add("apples")
    tree.add("bananas")
    tree.add("cucumbers")
    tree.add("dates")
    expected = ["apples", "bananas", "cucumbers", "dates"]
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected


@pytest.mark.skip("TODO")
def test_example_from_reading():
    """
    We build these out by hand because the example has some gaps
    i.e. it is not added to left-to-right
    """
    tree = BinaryTree()

    level_3_2 = Node(2)
    level_3_6 = Node(6, Node(5), Node(11))
    level_3_9 = Node(9, Node(4))

    level_2_left = Node(7, level_3_2, level_3_6)
    level_2_right = Node(5, right=level_3_9)

    tree._root = Node(2, level_2_left, level_2_right)

    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected
