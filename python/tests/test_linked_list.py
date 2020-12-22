from linked_list.linked_list import LinkedList, Node

def test_import():
    assert LinkedList

link = LinkedList()

def test_empty_list():
    actual = link.insert_node(None)
    value = None
    assert actual == value

def test_insert_list():
    actual = link.insert_node(4)
    value = None
    assert actual == value

def test_head_link():
    actual = str(link)
    value = '{4} -> {None} -> Null'
    assert actual == value

new_link = LinkedList()

def test_multiple_insert():
    new_link.insert_node(3)
    new_link.insert_node(6)
    new_link.insert_node(10)
    actual = str(new_link)
    value = '{10} -> {6} -> {3} -> Null'
    assert actual == value

def test_find_value():
    actual = new_link.search_node(3)
    value = True
    assert actual == value

def test_false_search():
    actual = new_link.search_node(99)
    value = False
    assert actual == value

def test_collection_of_all():
    actual = str(new_link)
    value = '{10} -> {6} -> {3} -> Null'
    assert actual == value