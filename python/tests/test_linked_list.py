from linked_list.linked_list import LinkedList, Node

import pytest

def test_import():
    assert LinkedList

def test_instance():
    finding_francis = LinkedList('goons')
    assert finding_francis.head
    
def test_node_import():
    assert Node

def test_node_instance_value():
    # !!! previously written in the syntax of 
    # `assert lackey.value` received linter error in spite of test passing.???
    lackey = Node('meat-head')
    actual = lackey.value
    expected = 'meat-head'
    assert actual == expected

def test_node_instance_reference():
    lackey = Node('meat-head')
    actual = lackey.next
    expected = None
    assert actual == expected

def test_llist_instance_insert():
    """testing when head was originally empty llist instance
    """
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    
    actual = finding_francis.head.value
    expected = 'meat-head'
    assert actual == expected
    
def test_llist_next_post_insert():
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    actual = finding_francis.head.next.value
    expected = 'goons'
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_next_of_origin_node():
    """tests next of the original head Node upon list instantiation
    """
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')
    actual = finding_francis.__str__()
    expected = '{ brown-pants } -> { meat-head } -> { goons } -> None '
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_includes_method_true():
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')
    finding_francis.insert('car-goon')
    
    assert finding_francis.includes('meat-head') == True

# @pytest.mark.skip('checking base')
def test_includes_method_false():
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')
    finding_francis.insert('car-goon')

    actual = finding_francis.includes('ryan-reynalds') 
    expected = False
    assert  actual == expected

# @pytest.mark.skip('checking base')
def test_str_of_llist_class():
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')
    finding_francis.insert('car-goon')

    actual = finding_francis.__str__()
    expected = '{ car-goon } -> { brown-pants } -> { meat-head } -> { goons } -> None '
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_append():
    finding_francis = LinkedList('goons')
    finding_francis.insert('meat-head')
    finding_francis.insert('brown-pants')

    finding_francis.append('car-goon')

    actual = finding_francis.__str__()
    expected = '{ brown-pants } -> { meat-head } -> { goons } -> { car-goon } -> None '
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_append_multiple():
    finding_francis = LinkedList('goons')

    finding_francis.append('meat-head')
    finding_francis.append('brown-pants')
    finding_francis.append('car-goon')

    actual = finding_francis.__str__()
    expected = '{ goons } -> { meat-head } -> { brown-pants } -> { car-goon } -> None '
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_insert_before_mid():
    finding_francis = LinkedList('goons')
    finding_francis.append('brown-pants')
    finding_francis.append('car-goon')
    
    finding_francis.insert_before('brown-pants', 'meat-head')

    actual = finding_francis.__str__()
    expected = '{ goons } -> { meat-head } -> { brown-pants } -> { car-goon } -> None '
    assert actual == expected

# @pytest.mark.skip('checking base')
def test_insert_before_first():
    finding_francis = LinkedList('goons') 
   
    finding_francis.append('brown-pants')
    finding_francis.append('car-goon')
    
    finding_francis.insert_before('goons', 'meat-head')

    actual = finding_francis.__str__()
    expected = '{ meat-head } -> { goons } -> { brown-pants } -> { car-goon } -> None '
    assert actual == expected

############
# Fixtures #
############

# initial attempt at using fixture revealed I need to understand their construction and behaavior better before implementing in code. TODO: when time permits, clean up testing by adding fixtures. 

# @pytest.fixture
# def finding_francis_data():
#     finding_francis = LinkedList('goons')
#     return finding_francis


# @pytest.fixture
# def lackey_data():
#     lackey = Node('lackey')
#     return lackey


# @pytest.fixture(autouse=True)
# def francis_not_here():
    # may not be need. I should see what returns when i use a fixture before constructing the cleanup function. 

