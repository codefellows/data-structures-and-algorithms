import pytest
from linked_list import LinkedList, TargetError


@pytest.mark.skip("TODO")
def test_kth_from_end_zero():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_kth_from_end_one():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_kth_from_end_two():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_kth_from_end_out_of_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


@pytest.mark.skip("TODO")
def test_kth_from_end_under_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


@pytest.mark.skip("TODO")
def test_kth_from_end_size_one():
    linked_list = LinkedList(values=["apples"])
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected
