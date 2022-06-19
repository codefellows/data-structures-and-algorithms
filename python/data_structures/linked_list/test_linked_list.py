import pytest
from data_structures.linked_list.linked_list import Node, LinkedList


def test_exists():
    assert LinkedList


#@pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


#@pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


#@pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


#@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "None"


#@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> None"


#@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> None"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> None"


#@pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


#@pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


@pytest.mark.skip("TODO")
def test_node_exists():
    assert Node

@pytest.mark.skip("TODO")
def test_create_node():
    node1 = Node(5)
    assert node1.value == 5

@pytest.mark.skip("TODO")
def test_create_node_not_pass():
    node1 = Node(5)
    assert node1.value != 6
