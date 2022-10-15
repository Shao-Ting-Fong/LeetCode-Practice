from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution 1: DP
        # Time Complexity:O(n)
        # Space Complexity: O(n)

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]

        return max(dp)