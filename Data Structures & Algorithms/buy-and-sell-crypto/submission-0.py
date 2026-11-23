class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [float("-inf")] * len(prices)
        max_profit = float("-inf")

        if len(prices) == 1: return 0
        min_stock = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(prices[i]-min_stock, max_profit)
            min_stock = min(min_stock, prices[i])
        
        print(profit)
        return 0 if max_profit <= 0 else max_profit
        