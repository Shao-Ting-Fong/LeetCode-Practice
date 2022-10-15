from typing import List

class Solution:

    # Solution 1: two-pointer
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        ans = set()

        for i, value in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if value + nums[left] + nums[right] > 0:
                    right -= 1
                elif value + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.add((value, nums[left], nums[right]))
                    left += 1

        return [*map(list, ans)]