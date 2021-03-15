import pytest
from hashtable.hashtable import Hashtable

new_hash = Hashtable()
new_hash.set('abc', 12)

# Adding a key/value to your hashtable results in the value being in the data structure
def test_hash1():
    hash_key = new_hash._hash('abc')
    current = new_hash._buckets[hash_key].head.value[1]
    actual = current
    expected = 12
    assert actual == expected

# Retrieving based on a key returns the value stored
def test_get():
    actual= new_hash.get('abc')
    expected = 12
    assert actual == expected

# Successfully handle a collision within the hashtable / Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_get2():
    new_hash.set('cab', 13)
    actual = new_hash.get('cab')
    expected = 13
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_get3():
    new_hash.set('cab', 13)
    new_hash.set('test', 33)
    new_hash.set('abc', 55)
    actual = new_hash.get('find')
    expected = None
    assert actual == expected

# Successfully hash a key to an in-range value
def test_contains():
    actual = new_hash.contains('abc')
    expected = True
    assert actual == expected

def test_contains_false():
    actual = new_hash.contains('bac')
    expected = False
    assert actual == expected