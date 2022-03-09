import pytest
from codefellows.dsa.binary_tree import BinaryTree
from code_challenges.tree_intersection import tree_intersection


def test_exists():
    assert tree_intersection


@pytest.mark.skip("TODO")
def test_tree_intersection():
    tree_a = BinaryTree(values=[150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500])
    tree_b = BinaryTree(values=[42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500])

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)
