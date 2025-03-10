from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Calculate the number of soldiers in each row and store (count, index)
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        
        # Sort based on number of soldiers, and if equal, by row index
        row_strength.sort()
        
        # Extract the first k indices
        return [row_strength[i][1] for i in range(k)]
