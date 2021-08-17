import pytest
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_curly():
    string = '{}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_three_brackets():
    string = '{}(){}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_extra_characters():
    string = '()[[Extra Characters]]'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_single_input():
    string = '('
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected

def test_two_false():
    string = '[}'
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected
