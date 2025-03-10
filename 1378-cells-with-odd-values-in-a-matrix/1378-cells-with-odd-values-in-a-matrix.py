from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        # Count row and column increments
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        # Count odd rows and columns
        odd_rows = sum(1 for x in row_count if x % 2 == 1)
        odd_cols = sum(1 for x in col_count if x % 2 == 1)
        
        # Calculate the number of odd cells
        return (odd_rows * (n - odd_cols)) + (odd_cols * (m - odd_rows))