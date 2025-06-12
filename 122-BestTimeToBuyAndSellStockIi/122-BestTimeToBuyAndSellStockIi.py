# Last updated: 6/11/2025, 10:34:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        
        total = 0

        for r in range(1, len(prices)):
            if prices[r-1] < prices[r]:
                profit = prices[r] - prices[r-1]
                print(profit)
                total += profit
        
        return total