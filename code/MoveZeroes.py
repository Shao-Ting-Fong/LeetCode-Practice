from typing import List

class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # fast: searching for non-zero element
        # swap element in position fast and slow if nums[slow] == 0
        # else slow += 1, searching for zero

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        # Brutal Force:TLE!
        slow = 0
        fast = 0

        while slow < len(nums) and fast < len(nums):

            while slow < len(nums) and nums[slow] != 0:
                slow += 1

            fast = slow + 1

            while fast < len(nums):
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    break
                else:
                    fast += 1
