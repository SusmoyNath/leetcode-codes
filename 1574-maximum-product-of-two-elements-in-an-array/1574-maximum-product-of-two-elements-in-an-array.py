from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        
        for num in nums:
            if num > max1:
                max2, max1 = max1, num  # Update max1 and shift max1 to max2
            elif num > max2:
                max2 = num  # Update max2 if it's smaller than max1
        
        return (max1 - 1) * (max2 - 1)
