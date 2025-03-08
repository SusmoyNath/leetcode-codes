from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points

        # Check if any two points are the same
        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
            return False

        # Check if the three points are collinear using the slope formula
        # The condition for collinearity: (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
