from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)  # Count frequencies
        return sorted(nums, key=lambda x: (freq[x], -x))  # Sort by (frequency, value in descending order)
