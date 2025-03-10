from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold, sell, cooldown = [0] * n, [0] * n, [0] * n
        
        hold[0] = -prices[0]  # If we buy on the first day
        
        for i in range(1, n):
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            cooldown[i] = max(cooldown[i-1], sell[i-1])
        
        return max(sell[-1], cooldown[-1])  # Max profit is either selling or cooldown
