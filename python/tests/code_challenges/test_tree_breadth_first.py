import pytest
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

    level_3_2 = _Node(2)
    level_3_6 = _Node(6, _Node(5), _Node(11))
    level_3_9 = _Node(9, _Node(4))

    level_2_left = _Node(7, level_3_2, level_3_6)
    level_2_right = _Node(5, right=level_3_9)

    tree._root = _Node(2, level_2_left, level_2_right)

    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected
