import pytest
from .hashtable_left_join import left_join
from .hashtable import Hashtable
#This is where the hashtable file would do if I had it fully working. Worked together with the team to make sure the tests and left_join function are working.


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_left_join():
    l_hash = Hashtable()
    r_hash = Hashtable()
    l_hash.set("diligent", "employed")
    l_hash.set("fond", "enamored")
    l_hash.set("guide", "usher")
    l_hash.set("outfit", "garb")
    l_hash.set("wrath", "anger")
    r_hash.set("diligent", "idle")
    r_hash.set("fond", "averse")
    r_hash.set("guide", "follow")
    r_hash.set("flow", "jam")
    r_hash.set("wrath", "delight")

    expected = [

        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", "None"],
        ["guide", "usher", "follow"],
        ["fond", "enamored", "averse"]
    ]

    actual = left_join(l_hash, r_hash)

    assert actual == expected


@pytest.mark.xfail
def test_left_join_xfail():
    l_hash = Hashtable()
    r_hash = Hashtable()
    l_hash.set("diligent", "employed")
    l_hash.set("fond", "enamored")
    l_hash.set("guide", "usher")
    l_hash.set("outfit", "garb")
    l_hash.set("wrath", "anger")
    r_hash.set("diligent", "idle")
    r_hash.set("fond", "averse")
    r_hash.set("guide", "follow")
    r_hash.set("flow", "jam")
    r_hash.set("wrath", "delight")

    expected = [

        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["guide", "usher", "follow"],
        ["fond", "enamored", "averse"]
    ]

    actual = left_join(l_hash, r_hash)

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_left_join_none():
    l_hash = Hashtable()
    r_hash = Hashtable()
    l_hash.set("diligent", "employed")
    l_hash.set("fond", "enamored")
    l_hash.set("guide", "usher")
    r_hash.set("truth", "no cap")
    r_hash.set("delicious", "bussin")
    r_hash.set("factual", "fake news")

    expected = [

        ["diligent", "employed", "None"],
        ["guide", "usher", "None"],
        ["fond", "enamored", "None"]
    ]

    actual = left_join(l_hash, r_hash)

    assert actual == expected
