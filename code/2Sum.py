from typing import List


class Solution:
    # Solution 1:
    # Use dictionary to keep previous value and the gap between it and target
    # Paring value in nums and keys in dic

    # Time  Complexity: O(n)
    # Space Complexity: O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for index, value in enumerate(nums):

            if (target - value) in dic:
                return [dic[target - value], index]

            else:
                dic[value] = index