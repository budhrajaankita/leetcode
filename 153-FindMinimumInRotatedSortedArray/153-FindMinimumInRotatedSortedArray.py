# Last updated: 6/11/2025, 10:34:49 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums)-1

        while lo < hi:
            mid = (lo+hi)//2

            if nums[mid] <= nums[hi]:
                hi = mid


            else:
                lo = mid + 1

        return nums[lo]




        
        