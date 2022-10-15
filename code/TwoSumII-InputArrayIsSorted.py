from typing import List

class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:

        # Solution 1:Hashmap
        # Time Complexity:O(n)
        # Space Complexity:O(n)

                d = {}

                for index, value in enumerate(numbers):
                    if (target - value) in d:
                        return [d[target - value], index + 1]
                    else:
                        d[value] = index + 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:

        # Solution 2: Two Pointer
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        left, right = 0, len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        # Solution 3: Binary Search
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)

        for index, value in enumerate(numbers):

            left, right = index + 1, len(numbers) - 1

            while left <= right:

                mid = left + (right - left) // 2

                if numbers[mid] == target - value:
                    return [index + 1, mid + 1]
                elif numbers[mid] < target - value:
                    left = mid + 1
                else:
                    right = mid - 1



