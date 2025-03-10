from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_cells = m * n
        k = k % total_cells  # Optimize k to avoid unnecessary full rotations
        
        # Flatten the grid into a 1D list
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Perform the shift
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        # Reshape back into a 2D grid
        return [flat_grid[i * n:(i + 1) * n] for i in range(m)]