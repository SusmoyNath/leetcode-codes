from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Get the first two points to determine initial slope
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        # Compute the slope differences
        dx = x2 - x1
        dy = y2 - y1
        
        # Check if all points maintain the same slope
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y - y1) * dx != (x - x1) * dy:
                return False
        
        return True