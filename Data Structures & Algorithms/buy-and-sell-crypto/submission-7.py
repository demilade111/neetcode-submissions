class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < cheapest_price:
                cheapest_price = price
            profit =  price - cheapest_price 
            max_profit = max(profit,max_profit)
        return max_profit

        