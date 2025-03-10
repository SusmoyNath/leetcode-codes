from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  # Sort the array
        num_to_count = {}  # Initialize the dictionary
        
        for idx, num in enumerate(sorted_nums):
            if num not in num_to_count:
                num_to_count[num] = idx

        return [num_to_count[num] for num in nums]
