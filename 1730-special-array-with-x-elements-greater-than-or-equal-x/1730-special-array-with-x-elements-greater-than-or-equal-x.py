from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()  # Sort in ascending order
        n = len(nums)
        
        for x in range(1, n + 1):  # Possible values of x are from 1 to n
            count = sum(1 for num in nums if num >= x)  # Count elements >= x
            if count == x:
                return x
        
        return -1  # If no x is found, return -1
