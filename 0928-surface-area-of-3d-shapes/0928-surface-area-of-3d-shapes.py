from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        surface_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Each stack contributes a top and bottom face
                    surface_area += 2 + 4 * grid[i][j]  # (top + bottom + 4 sides)
                    
                    # Remove overlap with previous row (above)
                    if i > 0:
                        surface_area -= 2 * min(grid[i][j], grid[i-1][j])
                    
                    # Remove overlap with previous column (left)
                    if j > 0:
                        surface_area -= 2 * min(grid[i][j], grid[i][j-1])
        
        return surface_area
