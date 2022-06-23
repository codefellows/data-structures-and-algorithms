import pytest
from .node import Node
from .stack import Stack
from .invalid_operation_error import InvalidOperationError


def test_node_exists():
    assert Node

#@pytest.mark.skip("TODO")
def test_create_node():
    node1 = Node(5)
    assert node1.value == 5

#@pytest.mark.skip("TODO")
def test_create_node_not_pass():
    node1 = Node(5)
    assert node1.value != 6


def test_exists():
    assert Stack


#@pytest.mark.skip("TODO")
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


#@pytest.mark.skip("TODO")
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


#@pytest.mark.skip("TODO")
def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"
