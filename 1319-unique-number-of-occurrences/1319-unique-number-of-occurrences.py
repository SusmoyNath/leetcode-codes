from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)  # Step 1: Count occurrences
        return len(set(freq.values())) == len(freq.values())  # Step 2: Check uniqueness