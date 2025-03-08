from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = sum(1 for x in position if x % 2 == 0)
        odd_count = len(position) - even_count
        return min(even_count, odd_count)
