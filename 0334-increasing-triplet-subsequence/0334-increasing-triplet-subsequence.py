from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  # Update second smallest
            else:
                return True  # Found a third element satisfying the condition
        
        return False  # No triplet found
