class Solution:

    def romanToInt(self, s: str) -> int:

        # Solution 1
        # Keys: read the string backwards
        # If the number is smaller than the number before it, substract the number

        translator = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        prev = 0

        for char in reversed(s):
            if translator[char] < prev:
                ans -= translator[char]
            else:
                ans += translator[char]

            prev = translator[char]

        return ans

    def romanToInt2(self, s: str) -> int:

        # Solution 2:
        # Good to understand but time-consuming due to multiple search

        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0

        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("IV", "IIII").replace("IX", "VIIII")

        for i in s:
            ans += d[i]

        return ans