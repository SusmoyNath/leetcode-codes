from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # Monotonic decreasing stack (stores indices)
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]  # Apply discount
            
            stack.append(i)  # Push current index onto the stack
        
        return prices
