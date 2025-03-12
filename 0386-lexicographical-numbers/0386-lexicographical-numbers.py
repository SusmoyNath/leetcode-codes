from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1  # Start from 1
        
        for _ in range(n):
            result.append(current)  # Add current number
            
            if current * 10 <= n:  
                current *= 10  # Move to the next depth (e.g., 1 â 10)
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10  # Move up (e.g., 19 â 1)
                current += 1  # Move to the next sibling
            
        return result
