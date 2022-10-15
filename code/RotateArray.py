from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        # e.g. nums = [1,2,3,4,5,6,7], k = 3
        # step 1: [7 6 5 | 4 3 2 1] (reverse all)
        # step 2: [5 6 7 | 4 3 2 1] (reverse index 0~k-1)
        # step 3: [5 6 7 | 1 2 3 4] (reverse index k~last)

        nums.reverse()
        k %= len(nums)

        self.partial_reverse(nums, 0, k - 1)
        self.partial_reverse(nums, k, len(nums) - 1)

    def partial_reverse(self, nums, start, end):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        # Solution 0:
        # if k > len(nums), swap k%len(nums) times instead of k
        # e.g. len(nums) = 7, k=8 --> same as k = 1, since the first 7 swaps
        # just return the same list, totally waste of time.

        # for i in range(k%len(nums)):
        #     nums.insert(0,nums.pop())
