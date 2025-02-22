class Solution(object):
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4  # Each land cell initially contributes 4

                    # Check adjacent cells and reduce perimeter for shared edges
                    if r > 0 and grid[r - 1][c] == 1:  # Check above
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:  # Check left
                        perimeter -= 2

        return perimeter
