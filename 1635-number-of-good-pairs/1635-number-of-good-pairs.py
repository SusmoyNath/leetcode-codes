from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)  # Count occurrences of each number
        good_pairs = 0
        
        # Calculate number of good pairs for each unique number
        for freq in count.values():
            good_pairs += (freq * (freq - 1)) // 2  # nC2 formula
        
        return good_pairs
