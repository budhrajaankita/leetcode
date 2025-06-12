# Last updated: 6/11/2025, 10:34:18 PM
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo = 1
        hi = max(candies)

        def calculate_piles(mid):
            total = 0

            for c in candies:
                total += c//mid
            return total

        max_candies = 0
        while lo <= hi:
            mid = (lo+hi) // 2

            if calculate_piles(mid) < k:
                hi = mid - 1
            else:
                lo = mid + 1
                max_candies = mid

        return max_candies
        