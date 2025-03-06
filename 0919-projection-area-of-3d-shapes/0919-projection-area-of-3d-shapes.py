from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        xy_projection = sum(1 for row in grid for cell in row if cell > 0)
        yz_projection = sum(max(col) for col in zip(*grid))  # Max in each column
        zx_projection = sum(max(row) for row in grid)  # Max in each row
        
        return xy_projection + yz_projection + zx_projection
