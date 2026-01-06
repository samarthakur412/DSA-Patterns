from typing import List


class solution:
    def maxprofit(self,prices:list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            
            profit = price - minPrice
            
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit
    

obj = solution()
print(obj.maxprofit([7,1,5,3,6,4]))