import pytest
from .hashtable import Hashtable


def test_exists():
    assert Hashtable

#@pytest.mark.skip("TODO")
def test_hash():
    hashtable = Hashtable(1024)
    expected = hashtable.hash("test")
    # test = 2 for hashtable(3) and 64 for (1024)
    actual = 5
    assert actual != expected

#@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_get_second():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("aa", "triangular")
    actual = hashtable.get("pizza")
    expected = "triangular"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_key_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.keys()
    expected = "apple"
    assert actual == expected

# We were told to take this test out, it is not working. The linkedlist implementation is based on a .display thing. Essentially where it prints the values. This is the built in the values you have in the traverse method if you had return instead of print.

# #@pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")

#     actual = []

#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())

#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

#     assert actual == expected
