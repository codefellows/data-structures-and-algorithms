from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    to_return = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if target == (nums[i] + nums[j]):
                    to_return = [i, j]
                    return to_return       
