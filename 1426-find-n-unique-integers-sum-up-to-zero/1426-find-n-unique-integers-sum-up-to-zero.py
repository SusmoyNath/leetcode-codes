from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # If n is odd, include 0
        if n % 2 == 1:
            result.append(0)
        
        # Add pairs of negative and positive numbers
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        return result
