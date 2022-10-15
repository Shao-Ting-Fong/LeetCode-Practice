class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # used負責記錄出現過的字母上次出現的位置
        # [start, end]圍出可能為最常字串的空間(Sliding window)
        # end不斷前進，檢查是否有重複字母且出現在Sliding window中
        # 若有，更新start的位置至重複字母的下一格

        used = {}
        start = max_length = 0

        for end, value in enumerate(s):
            if value in used and start <= used[value]:
                start = used[value] + 1
            else:
                max_length = max(max_length, end - start + 1)

            used[value] = end

        return max_length
