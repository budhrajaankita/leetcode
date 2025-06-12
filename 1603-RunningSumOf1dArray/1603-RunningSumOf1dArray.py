# Last updated: 6/11/2025, 10:34:17 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        sum_list = []
        for i in nums:
            sum+= i
            sum_list.append(sum)
        return sum_list