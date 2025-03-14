from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -1  # Initialize last seen index of '1' as -1
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_index != -1 and i - last_index - 1 < k:
                    return False  # Distance is less than k
                last_index = i  # Update last seen index
        
        return True
