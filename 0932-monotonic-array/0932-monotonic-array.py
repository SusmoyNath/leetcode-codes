from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False  # Not monotonic decreasing
            if nums[i] < nums[i - 1]:
                increasing = False  # Not monotonic increasing

        return increasing or decreasing
