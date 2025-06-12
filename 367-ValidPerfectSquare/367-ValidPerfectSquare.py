# Last updated: 6/11/2025, 10:34:31 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num

        
        while lo <= hi:
            mid = (lo + hi) //2

            if mid**2 == num:
                return True
            if num > mid**2:
                lo=mid+1
            else:
                hi = mid - 1
        
        return False