from linked_list.linked_list import LinkedList, Node

def test_import():
    assert LinkedList

# Code Challenge 06 

# Add a node to the end of the linked list
def test_append():
    node = Node(0)
    link = LinkedList(node)
    link.insert_node(4)
    link.append(10)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
    assert actual == expected

# Can successfully add multiple nodes to the end of a linked list
def test_multi_append():
    link = LinkedList()
    link.insert_node(4)
    link.append(1)
    link.append(2)
    link.append(3)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 1 }} -> {{ 2 }} -> {{ 3 }} -> NULL'
    
# Insert a node before a node located in the middle of a linked list
def test_before():
    node = Node(0)
    link = LinkedList(node)
    link.insert_node(4)
    link.append(10)
    link.insert_before(0, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
    assert actual == expected

# Can successfully insert a node before the first node of a linked list
def test_before_first():
    node = Node(0)
    link = LinkedList(node)
    link.insert_node(4)
    link.append(10)
    link.insert_node(5)
    actual = str(link)
    expected = f'{{ 5 }} -> {{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
    assert actual == expected

# Can successfully insert after a node in the middle of the linked list
def test_after():
    node = Node(0)
    link = LinkedList(node)
    link.insert_node(4)
    link.append(10)
    link.insert_after(0, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 5 }} -> {{ 10 }} -> NULL'
    assert actual == expected

# Can successfully insert a node after the last node of the linked list
def test_after_last():
    node = Node(0)
    link = LinkedList(node)
    link.insert_node(4)
    link.append(10)
    link.insert_after(10, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> {{ 5 }} -> NULL'
    assert actual == expected

# Code challenge 04 stuff
# link = LinkedList()

# def test_empty_list():
#     actual = link.insert_node(None)
#     value = None
#     assert actual == value

# def test_insert_list():
#     actual = link.insert_node(4)
#     value = None
#     assert actual.value == value

# def test_head_link():
#     actual = str(link)
#     value = '{4} -> {None} -> Null'
#     assert actual == value

# new_link = LinkedList()

# def test_multiple_insert():
#     new_link.insert_node(3)
#     new_link.insert_node(6)
#     new_link.insert_node(10)
#     actual = str(new_link)
#     value = '{10} -> {6} -> {3} -> Null'
#     assert actual == value

# def test_find_value():
#     actual = new_link.search_node(3)
#     value = True
#     assert actual == value

# def test_false_search():
#     actual = new_link.search_node(99)
#     value = False
#     assert actual == value

# def test_collection_of_all():
#     actual = str(new_link)
#     value = '{10} -> {6} -> {3} -> Null'
#     assert actual == value