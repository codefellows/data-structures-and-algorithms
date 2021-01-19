import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_input_empty():
  actual = multi_bracket_validation('')
  expected = f'Cannot validate empty string'
  assert actual == expected

def test_input_not_string():
  actual_1 = multi_bracket_validation([])
  expected_1 = 'Cannot validate input of type: <class \'list\'>'
  assert actual_1 == expected_1
  actual_2 = multi_bracket_validation(('a', 'b'))
  expected_2 = 'Cannot validate input of type: <class \'tuple\'>'
  assert actual_2 == expected_2
  actual_3 = multi_bracket_validation({'key' : 'value'})
  expected_3 = 'Cannot validate input of type: <class \'dict\'>'
  assert actual_3 == expected_3
  actual_4 = multi_bracket_validation(4)
  expected_4 = 'Cannot validate input of type: <class \'int\'>'
  assert actual_4 == expected_4

def test_input_with_full_parens():
  actual = multi_bracket_validation('(coords)')
  expected = True
  assert actual == expected

def test_input_with_full_square():
  actual = multi_bracket_validation('[x, y]')
  expected = True
  assert actual == expected

def test_input_with_full_mustaches():
  actual = multi_bracket_validation('{key : value}')
  expected = True
  assert actual == expected

def test_input_with_all_full():
  actual = multi_bracket_validation('(coords) [x, y] {key : value}')
  expected = True
  assert actual == expected

def test_input_with_partial_parens():
  actual = multi_bracket_validation('(coords')
  expected = False
  assert actual == expected

def test_input_with_partial_square():
  actual = multi_bracket_validation('x, y]')
  expected = False
  assert actual == expected

def test_input_with_partial_mustaches():
  actual = multi_bracket_validation('{key : value')
  expected = False
  assert actual == expected

def test_input_with_all_partial():
  actual = multi_bracket_validation('coords) [x, y key : value}')
  expected = False
  assert actual == expected

def test_input_with_mixed_partials():
  actual = multi_bracket_validation('(coords) [x, y {key : value}')
  expected = False
  assert actual == expected

