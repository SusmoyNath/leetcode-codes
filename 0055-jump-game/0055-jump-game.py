from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Tracks the farthest index we can reach
        
        for i in range(len(nums)):
            if i > farthest:
                return False  # If we can't reach this index, return False
            
            farthest = max(farthest, i + nums[i])  # Update max reachable index
            
            if farthest >= len(nums) - 1:  # If we can reach the last index, return True
                return True
        
        return False
