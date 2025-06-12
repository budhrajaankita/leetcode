# Last updated: 6/11/2025, 10:34:39 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = n * (n+1) // 2

        return actual - sum(nums)