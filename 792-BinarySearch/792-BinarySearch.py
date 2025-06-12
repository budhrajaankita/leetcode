# Last updated: 6/11/2025, 10:34:25 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1

        while lo <= hi:
            mid = lo +(hi-lo) // 2

            if target > nums[mid]:
                lo = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                hi = mid-1

        return -1