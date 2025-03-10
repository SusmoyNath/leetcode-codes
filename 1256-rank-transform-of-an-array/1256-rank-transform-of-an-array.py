from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted list of unique elements
        sorted_unique = sorted(set(arr))
        
        # Assign ranks to unique elements
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        # Transform the original array based on ranks
        return [rank_map[num] for num in arr]
