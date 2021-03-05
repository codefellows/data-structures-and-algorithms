from merge_sort.merge_sort import mergeSort

def test_merge_sort():
    arr = [8,4,23,42,16,15]
    actual = mergeSort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_merge_sort2():
    arr = [20,18,12,8,5,-2]
    actual = mergeSort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_merge_sort3():
    arr = [5,12,7,5,5,7]
    actual = mergeSort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_merge_sort3():
    arr = [2,3,5,7,13,11]
    actual = mergeSort(arr)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected