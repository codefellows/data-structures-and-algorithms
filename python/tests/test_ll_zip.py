import pytest
from code_challenges.ll_zip.ll_zip import zip_lists

from linked_list.linked_list import LinkedList, Node


  
# @pytest.mark.skipped('pending-code')
# def test_fixture_first_list():
#   first_list = LinkedList()
#   first_list.append(3)
#   first_list.append(6)
#   first_list.append(8)

#   sec_list = LinkedList()
#   sec_list.append(4)
#   sec_list.append(7)
#   sec_list.append(9)
#   sec_list.append(11)

#   assert first_list.__str__() == '{{ {3} }} -> {{ {6} }} -> {{ {8} }} -> None '


# @pytest.skipped('pending-code')
def test_zip_lists_output_len():
  first_list = LinkedList()
  first_list.append(3)
  first_list.append(6)
  first_list.append(8)

  sec_list = LinkedList()
  sec_list.append(4)
  sec_list.append(7)
  sec_list.append(9)
  sec_list.append(11)
  
  zip_lists(first_list, sec_list)
  assert first_list.kth_from_end(1) == 11





# @pytest.skipped('pending-code')
# def test_ll_zip_value_alternation():
  


# @pytest.fixture
# def first_list():
#   first_list = LinkedList()
#   first_list.append(3)
#   first_list.append(6)
#   first_list.append(8)
