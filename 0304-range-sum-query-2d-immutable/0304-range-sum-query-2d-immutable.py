from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:  
            return 
        
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]  # Extra row/col for easier calculations
        
        # Build prefix sum matrix
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = (
                    matrix[i][j] +
                    self.prefix[i][j+1] +
                    self.prefix[i+1][j] -
                    self.prefix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2+1][col2+1] -
            self.prefix[row1][col2+1] -
            self.prefix[row2+1][col1] +
            self.prefix[row1][col1]
        )
