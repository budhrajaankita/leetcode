# Last updated: 5/9/2025, 4:53:41 PM
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        i = 1
        curr = 0
        score = 0

        while i < len(nums):
            if (i==len(nums)-1) or (nums[curr] < nums[i]):
                score += (i-curr) * nums[curr]
            
                curr = i
            i+=1
        
        return score


