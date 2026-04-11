class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0   # Pointer to track the day to buy
        sell = 1  # Pointer to track the day to sell (always ahead of buy)
        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                # We can make a profit
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                # Found a lower price to buy
                buy = sell
            sell += 1  # Always move the sell pointer forward

        return max_profit
            


        