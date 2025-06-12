# Last updated: 6/11/2025, 10:35:09 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid
            
            elif nums[mid] >= nums[lo]:
                # left sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            elif nums[mid] <= nums[hi]:
                # right sorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
        return -1




        