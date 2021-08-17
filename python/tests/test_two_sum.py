from array_challenges.two_sum.two_sum import twoSum

def test_one():
    nums = [2,7,11,15]
    target = 9
    actual = twoSum(nums, target)
    expected = [0, 1]
    assert actual == expected
