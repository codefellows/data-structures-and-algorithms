from quicksort.quicksort import quicksort

arr1 = [8, 4, 23, 42, 16, 15]
right = len(arr1) - 1

def test_arr1_qs():
    actual = quicksort(arr1, 0, right)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

arr2 = [20,18,12,8,5,-2]
right = len(arr2) - 1

def test_arr2_qs():
    actual = quicksort(arr2, 0, right)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

arr3 = [5,12,7,5,5,7]
right = len(arr3) - 1

def test_arr3_qs():
    actual = quicksort(arr3, 0, right)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected