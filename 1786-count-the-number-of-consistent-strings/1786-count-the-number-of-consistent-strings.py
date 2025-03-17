from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert allowed string to a set for O(1) lookup
        return sum(set(word).issubset(allowed_set) for word in words)
