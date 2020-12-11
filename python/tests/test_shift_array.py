from array_shift.array_shift import insertShiftArray

def test_initial():
    assert insertShiftArray

arg = [2,4,6,8]
arg2 = [2,3,4,6,8]
num = 5

def test_shift_even():
    actual = insertShiftArray(arg, num)
    value = [2,4,5,6,8]
    assert actual == value
    # assert insertShiftArray

def test_shift_odd():
    actual = insertShiftArray(arg2, num)
    value = [2,3,4,5,6,8]
    assert actual == value
    # assert insertShiftArray