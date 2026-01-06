from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(1, len(prices)):
            # If the current price is higher than the previous day's price, we have a profit opportunity:
            if prices[i] > prices[i - 1]:
                # Accumulate the profit by subtracting yesterday's price from today's price.
                maxProfit += prices[i] - prices[i - 1]
        
        # At the end, maxProfit holds the total profit accrued through all transactions.
        return maxProfit