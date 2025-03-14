from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0  # Counter for consecutive odd numbers
        
        for num in arr:
            if num % 2 == 1:  # Check if the number is odd
                count += 1
                if count == 3:
                    return True  # Found three consecutive odd numbers
            else:
                count = 0  # Reset counter if an even number is encountered
        
        return False  # No three consecutive odds found
