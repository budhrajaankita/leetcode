# Last updated: 6/11/2025, 10:35:04 PM
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero=0
        two=len(nums)-1
        curr =0

        while curr <= two:

            if nums[curr] == 0:
                nums[curr], nums[zero] = nums[zero], nums[curr]
                curr += 1
                zero += 1

            elif nums[curr] == 1:
                curr += 1

            elif nums[curr] == 2:
                nums[curr], nums[two] = nums[two], nums[curr]
                two -= 1


2,0,1

1,0,2




