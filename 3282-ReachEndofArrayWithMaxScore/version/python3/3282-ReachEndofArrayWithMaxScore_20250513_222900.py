# Last updated: 5/13/2025, 10:29:00 PM
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        i = 0
        score = 0

        for j in range(1, len(nums)):

            if j == len(nums)-1 or nums[j] > nums[i]:
                score += (j-i) * nums[i]
                i = j
        return score



