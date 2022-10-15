import math

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start_time = 60 * int(loginTime[:2]) + int(loginTime[-2:])
        end_time = 60 * int(logoutTime[:2]) + int(logoutTime[-2:])

        # end_time // 15 is equal to math.floor
        # replace (start+14) / 15 with math.ceil if import math is prohibited
        ans = end_time // 15 - math.ceil(start_time / 15)
        ans += (start_time > end_time) * 96

        # Edge Case: "00:14" -> "00:27", should be 0, not -1
        return max(0, ans)