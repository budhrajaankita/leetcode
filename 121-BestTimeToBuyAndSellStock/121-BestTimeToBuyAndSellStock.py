# Last updated: 6/11/2025, 10:34:56 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if minPrice > price:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit