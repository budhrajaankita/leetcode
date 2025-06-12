# Last updated: 6/11/2025, 10:34:40 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        for i in range(len(nums)-1, -1,-1):
            output[i] *= right
            right *= nums[i]

        return output