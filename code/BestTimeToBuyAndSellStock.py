from typing import List

class Solution:
    # Solution 1: Dynamic Programming
    # TIme Complexity: O(n)
    # Space Complexity:O(1)

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = prices[0]
        # Slicing Complexity: O(k), where k is the size you slice out

        for i in range(1, len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                profit = prices[i] - cur_min
                if profit > max_profit:
                    max_profit = profit
        return max_profit
