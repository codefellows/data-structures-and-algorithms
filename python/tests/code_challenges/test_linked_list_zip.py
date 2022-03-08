import pytest
from code_challenges.linked_list_zip import zip_lists


def test_exists():
    assert zip_lists


@pytest.mark.skip("TODO")
def test_even_length():
    list_a = LinkedList(values=[1, 2, 3])
    list_b = LinkedList(values=["a", "b", "c"])
    zipped = zip_linked_lists(list_a, list_b)
    solution = LinkedList(values=[1, "a", 2, "b", 3, "c"])
    assert zipped == solution, zipped


@pytest.mark.skip("TODO")
def test_a_shorter():
    list_a = LinkedList(
        values=[
            1,
            2,
        ]
    )
    list_b = LinkedList(values=["a", "b", "c"])
    zipped = zip_linked_lists(list_a, list_b)
    solution = LinkedList(values=[1, "a", 2, "b", "c"])
    assert zipped == solution, zipped


@pytest.mark.skip("TODO")
def test_b_shorter():
    list_a = LinkedList(values=[1, 2, 3])
    list_b = LinkedList(
        values=[
            "a",
            "b",
        ]
    )
    zipped = zip_linked_lists(list_a, list_b)
    solution = LinkedList(
        values=[
            1,
            "a",
            2,
            "b",
            3,
        ]
    )
    assert zipped == solution, zipped


@pytest.mark.skip("TODO")
def test_a_empty():
    list_a = LinkedList()
    list_b = LinkedList(values=["a", "b", "c"])
    zipped = zip_linked_lists(list_a, list_b)
    solution = LinkedList(values=["a", "b", "c"])
    assert zipped == solution, zipped


@pytest.mark.skip("TODO")
def test_b_empty():
    list_a = LinkedList(values=[1, 2, 3])
    list_b = LinkedList()
    zipped = zip_linked_lists(list_a, list_b)
    solution = LinkedList(values=[1, 2, 3])
    assert zipped == solution, zipped
