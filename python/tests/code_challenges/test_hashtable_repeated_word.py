import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word


@pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected
