from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Generate all cell coordinates in the matrix
        cells = [(r, c) for r in range(rows) for c in range(cols)]
        
        # Sort by Manhattan distance from (rCenter, cCenter)
        cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
        
        return cells