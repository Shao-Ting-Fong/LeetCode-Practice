class Solution:
    def reverseWords(self, s: str) -> str:

        # Solution 1: build-in function
        # return ' '.join([ele[::-1] for ele in s.split(' ')])

        # Solution 2: Two pointers
        start, end = 0, 0

        while end < len(s):
            if s[end] == ' ':
                s = s[:start] + s[start:end][::-1] + s[end:]
                start = end + 1
            end += 1

        s = s[:start] + s[start:][::-1]

        return s
