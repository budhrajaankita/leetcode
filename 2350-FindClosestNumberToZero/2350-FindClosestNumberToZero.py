# Last updated: 6/11/2025, 10:34:14 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minm = inf

        for i in nums:
            if abs(i) < minm :
                minm = abs(i)
        
        neg = -minm

        if neg in nums and minm not in nums:
            return neg
        else:
            return minm        