# Last updated: 4/1/2025, 11:33:57 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        if target < nums[lo]:
            return 0
        elif target > nums[hi]:
            return len(nums)

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        if nums[mid] < target:
            return mid + 1
        else:
            return mid


    