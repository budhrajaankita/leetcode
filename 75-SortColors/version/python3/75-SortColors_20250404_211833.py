# Last updated: 4/4/2025, 9:18:33 PM
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        curr = 0
        l = 0
        r = len(nums) - 1

        while curr <= r:

            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                curr += 1

            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1

            else:
                curr += 1



        