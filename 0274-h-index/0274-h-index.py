from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort in descending order
        h = 0
        
        for i, cite in enumerate(citations):
            if cite >= i + 1:
                h = i + 1
            else:
                break  # Stop when condition is violated
        
        return h
