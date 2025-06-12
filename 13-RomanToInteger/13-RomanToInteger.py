# Last updated: 6/11/2025, 10:35:12 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0

        for rom in range(len(s)-1, -1, -1):
            if rom < len(s)-1 and d[s[rom]] < d[s[rom+1]]:
                val -= d[s[rom]]
            else:
                val += d[s[rom]]

        return val