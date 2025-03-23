# Last updated: 3/23/2025, 4:10:31 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit 

        