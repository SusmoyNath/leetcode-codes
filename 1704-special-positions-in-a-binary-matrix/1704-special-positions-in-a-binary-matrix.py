from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])  # Get matrix dimensions
        
        # Step 1: Compute row and column sums
        row_count = [sum(row) for row in mat]   # Number of 1s in each row
        col_count = [sum(mat[i][j] for i in range(m)) for j in range(n)]  # Number of 1s in each column
        
        # Step 2: Check for special positions
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1
        
        return special_count
