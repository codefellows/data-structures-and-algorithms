import pytest
from fizz_buzz_tree.fizz_buzz_tree import K_AryTree, K_node

@pytest.fixture()
def test_fb_tree():
    node_alpha = K_node(3)
    node_bravo = K_node(4)
    node_charlie = K_node(5)
    node_delta = K_node(6)
    node_echo = K_node(7)
    node_foxtrot = K_node(8)
    node_golf = K_node(9)
    node_hotel = K_node(10)
    node_india = K_node(11)
    node_juliet = K_node(12)
    node_kilo = K_node(13)
    node_lima = K_node(14)
    node_mike = K_node(15)

    node_alpha.children.append(node_bravo)
    node_alpha.children.append(node_charlie)
    node_alpha.children.append(node_delta)

    node_bravo.children.append(node_echo)
    node_bravo.children.append(node_foxtrot)
    node_bravo.children.append(node_golf)

    node_charlie.children.append(node_hotel)
    node_charlie.children.append(node_india)
    node_charlie.children.append(node_juliet)

    node_delta.children.append(node_kilo)
    node_delta.children.append(node_lima)
    node_delta.children.append(node_mike)

    test_K_tree = K_AryTree(node_alpha)

    return test_K_tree


def test_fizz_buzz_root(test_fb_tree):
    tree, nodes = test_fb_tree.fizz_buzz_tree()
    actual = tree.root.value
    expected = 'Fizz'
    assert actual == expected


def test_fizz_buzz_structure(test_fb_tree):
    tree, actual = test_fb_tree.fizz_buzz_tree()
    expected = ['Fizz', '4', '7', '8', 'Fizz', 'Buzz',
                'Buzz', '11', 'Fizz', 'Fizz', '13', '14', 'FizzBuzz']
    assert actual == expected