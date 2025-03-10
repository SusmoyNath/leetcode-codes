from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4  # More than 25% means appearing more than len(arr) // 4 times
        count = Counter(arr)  # Count occurrences of each number
        
        for num, freq in count.items():
            if freq > threshold:
                return num