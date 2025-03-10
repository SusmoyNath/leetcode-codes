from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect cycle using Floydâs Tortoise and Hare algorithm
        slow, fast = nums[0], nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]  # Move 1 step
            fast = nums[nums[fast]]  # Move 2 steps
        
        # Step 2: Find the entry point of the cycle (duplicate number)
        slow = 0  # Reset slow to start
        while slow != fast:
            slow = nums[slow]  # Move 1 step
            fast = nums[fast]  # Move 1 step
        
        return slow  # The duplicate number
