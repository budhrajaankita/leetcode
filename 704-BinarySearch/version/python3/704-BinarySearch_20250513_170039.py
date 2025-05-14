# Last updated: 5/13/2025, 5:00:39 PM
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