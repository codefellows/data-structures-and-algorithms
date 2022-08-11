from .merge_code import merge_sort

def test_function_exists():
    assert merge_sort

def test_regular():
    test_array = [8,4,23,42,16,15]
    result_array =  merge_sort(test_array)
    expected = [4,8,15,16,23,42]
    assert result_array == expected

def test_regular_odd():
    test_array = [8,4,23,42,16,15,100]
    result_array =  merge_sort(test_array)
    expected = [4,8,15,16,23,42,100]
    assert result_array == expected

def test_reversed():
    test_array = [20,18,12,8,5,-2]
    result_array =  merge_sort(test_array)
    expected = [-2,5,8,12,18,20]
    assert result_array == expected

def test_repeating():
    test_array = [5,12,7,5,5,7]
    result_array =  merge_sort(test_array)
    expected = [5,5,5,7,7,12]
    assert result_array == expected

def test_almost_sorted():
    test_array = [2,3,5,7,13,11]
    result_array =  merge_sort(test_array)
    expected = [2,3,5,7,11,13]
    assert result_array == expected

def test_empty():
    test_array = []
    result_array =  merge_sort(test_array)
    expected = []
    assert result_array == expected

def test_one():
    test_array = [9]
    result_array =  merge_sort(test_array)
    expected = [9]
    assert result_array == expected
