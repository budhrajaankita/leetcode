# Last updated: 3/24/2025, 1:21:37 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = n * (n+1) // 2

        return actual - sum(nums)