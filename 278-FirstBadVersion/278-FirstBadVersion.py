# Last updated: 6/11/2025, 10:34:37 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n

        while lo < hi:
            mid = (lo + hi) // 2

            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return hi