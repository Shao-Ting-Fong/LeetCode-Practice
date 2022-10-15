class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(26*2) = O(1)

        # 如果硬是算出s1所有排列再一個一個找s2有沒有包含，時間複雜度變成n! -> TLE
        # 核心想法：只需要s2的substring和s1「字母出現次數」相同，substring就必為s1的排列
        # 建立兩個dict，freq_s1和freq_s2，前者紀錄s1字母出現的次數
        # 後者走訪s2，每個和s1長度相同的substring，記錄他們字母出現的次數
        # 一旦兩個dict相同，return True

        if len(s1) > len(s2): return False

        freq_s1 = {chr(i): 0 for i in range(97, 123)}
        freq_s2 = {chr(i): 0 for i in range(97, 123)}

        for char in s1:
            freq_s1[char] += 1

        for index, value in enumerate(s2):
            if index >= len(s1):
                freq_s2[s2[index - len(s1)]] -= 1

            freq_s2[value] += 1

            if freq_s1 == freq_s2: return True

        return False
