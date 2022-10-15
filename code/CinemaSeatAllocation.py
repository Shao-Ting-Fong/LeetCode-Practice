from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        Time Complexity: O(M+N),
        which M is the length of reservedSeats, N is the number of rows been reserved

        Space Complexity: O(n)

        Seats could be divided into three sections:

        Left: [2,3,4,5]
        Mid:  [4,5,6,7]
        Right:[6,7,8,9]

        If any seats in the section is reserved, the four-persons group can't sit there

        """
        ans = 2 * n

        if not reservedSeats:  # All the seats are not reserved
            return ans

        seats = defaultdict(set)  # use set() to avoid repeat element

        for row, col in reservedSeats:

            if col in [2, 3, 4, 5]:
                seats[row].add("Left")
            if col in [4, 5, 6, 7]:
                seats[row].add("Mid")
            if col in [6, 7, 8, 9]:
                seats[row].add("Right")

        for ele in seats.values():
            if len(ele) == 3:
                ans -= 2
            else:
                ans -= 1

        return ans
