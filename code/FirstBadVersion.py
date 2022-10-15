# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion1(self, n: int) -> int:
        # Solution 1: brutal force
        # Time Complexity: O(n)

        for i in range(1,n+1):
            if isBadVersion(i):
                return i

    def firstBadVersion2(self, n: int) -> int:

        # Solution 2: binary search
        # Time Complexity: O(logn)

        # 和 #704不同的地方在於，這題是要找第一個出現錯誤的位置
        # 發現mid是錯誤的，right = mid，找尋前面還有沒有錯誤
        # 發現mid是正確的，代表他的前面都是對的，left = mid + 1，繼續尋找
        # 回傳值要是left，代表第一個出錯的位置

        left, right = 1, n

        while left < right:

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left



