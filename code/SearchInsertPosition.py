from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Solution 1: binary search
        left, right = 0, len(nums) - 1

        while left < right:

            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left + 1 if nums[left] < target else left

        # Solution 0: Use bisect_left --> cheat!
        # return bisect_left(nums, target)