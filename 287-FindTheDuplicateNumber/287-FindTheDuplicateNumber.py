# Last updated: 6/11/2025, 10:34:36 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        d = {}

        for n in nums:
            if n in d:
                return n
            d[n] = 0

        