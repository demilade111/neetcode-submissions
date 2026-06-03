class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < cheapest_price: 
              cheapest_price = price
            else:
                profit = price - cheapest_price
                if profit > max_profit:
                    max_profit = profit
            
        return max_profit 
        


