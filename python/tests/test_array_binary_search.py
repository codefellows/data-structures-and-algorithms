from code_challenges.array_binary_search.array_binary_search import search_by_iterator, array_binary_search


# test Iterator
def test_search_by_iterator_true():
  actual = search_by_iterator([1, 3, 6, 12, 24], 12)
  expected = 3
  assert actual == expected

def test_search_by_iterator_false():
  actual = search_by_iterator([1, 3, 6, 12, 24], 4)
  expected = -1
  assert actual == expected

def test_array_binary_search_true():
  actual = array_binary_search([1, 3, 6, 12, 24], 12)
  expected = 3
  assert actual == expected

def test_array_binary_search_false():
  actual = array_binary_search([1, 3, 6, 12, 24], 4)
  expected -1
  assert actual == expected

