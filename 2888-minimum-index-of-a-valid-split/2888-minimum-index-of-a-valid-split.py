from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element
        freq = Counter(nums)
        dominant = max(freq, key=freq.get)  # The element with the highest frequency
        total_count_x = freq[dominant]

        # Step 2: Check for the minimum valid split
        count_x_left = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == dominant:
                count_x_left += 1
            
            count_x_right = total_count_x - count_x_left
            size_left = i + 1
            size_right = n - size_left

            if count_x_left * 2 > size_left and count_x_right * 2 > size_right:
                return i
        
        return -1
