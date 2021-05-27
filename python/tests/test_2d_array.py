import pytest
from two_d_array.two_d_array import hourglassSum

@pytest.fixture()
def make_2_d_array():
    two_d_arr = []
    for i in range(0, 6):
        two_d = []
        for j in range(0, 6):
            two_d.append(1 + i)
        two_d_arr.append(two_d)
    return two_d_arr

def test_two_d_array(make_2_d_array):
    two_d = make_2_d_array
    print(two_d)
    result = hourglassSum(two_d)
    expected = 35
    assert result == expected