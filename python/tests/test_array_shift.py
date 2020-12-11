from code_challenges.array_shift.array_shift import insert_shift_array


def test_insert_shift_array_even_len():
  actual = insert_shift_array(3, [1, 2, 4, 5])
  expected = [1, 2, 3, 4, 5]
  assert actual == expected

def test_insert_shift_array_odd_len():
  actual = insert_shift_array(3, [1, 2, 4, 5, 6])
  expected = [1, 2, 4, 3, 5, 6]
  assert actual == expected

