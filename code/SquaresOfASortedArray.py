from typing import List

class Solution:
    # Time Complexity: O(n)
    # Worse case: all negative / all positive
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] **2 > nums[right] ** 2:
                ans.insert(0, nums[left]**2)
                left += 1
            else:
                ans.insert(0, nums[right]**2)
                right -= 1

        return ans