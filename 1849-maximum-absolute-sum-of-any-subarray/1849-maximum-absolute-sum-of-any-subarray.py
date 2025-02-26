from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0  # Stores the max positive subarray sum
        min_sum = 0  # Stores the min negative subarray sum
        curr_max = 0  # Current max subarray sum
        curr_min = 0  # Current min subarray sum

        for num in nums:
            curr_max = max(curr_max + num, num)  # Kadaneâs for max sum
            curr_min = min(curr_min + num, num)  # Kadaneâs for min sum
            
            max_sum = max(max_sum, curr_max)  # Update global max sum
            min_sum = min(min_sum, curr_min)  # Update global min sum

        return max(max_sum, abs(min_sum))  # Return max absolute sum
