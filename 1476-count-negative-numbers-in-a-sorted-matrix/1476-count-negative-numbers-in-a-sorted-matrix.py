from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # Get matrix dimensions
        row, col = 0, n - 1  # Start from the top-right corner
        count = 0
        
        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += (m - row)  # All numbers below this are negative
                col -= 1  # Move left
            else:
                row += 1  # Move down
        
        return count