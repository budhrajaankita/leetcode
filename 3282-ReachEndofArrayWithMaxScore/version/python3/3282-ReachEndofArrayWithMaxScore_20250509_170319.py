# Last updated: 5/9/2025, 5:03:19 PM
# class Solution:
#     def findMaximumScore(self, nums: List[int]) -> int:
#         j = 1
#         i = 0
#         score = 0

#         while i < len(nums):
#             if (i==len(nums)-1) or (nums[i] < nums[j]):
#                 score += (j-i) * nums[i]
#                 i = j
#             i+=1
        
#         return score


class Solution:
    def findMaximumScore(self, arr: List[int]) -> int:
        ans=0 
        prev=arr[0]
        arr.pop()
        for i in arr:
            if i>prev:
                prev=i
            ans+=prev
        return ans