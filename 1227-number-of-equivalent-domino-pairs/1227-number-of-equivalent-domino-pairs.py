from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)  # Hash map to store frequency of each unique domino
        pairs = 0  # Store the count of equivalent pairs
        
        for a, b in dominoes:
            key = tuple(sorted([a, b]))  # Sort to handle rotation cases (1,2) == (2,1)
            pairs += count[key]  # Add existing pairs count for this key
            count[key] += 1  # Increment frequency of this domino type
        
        return pairs