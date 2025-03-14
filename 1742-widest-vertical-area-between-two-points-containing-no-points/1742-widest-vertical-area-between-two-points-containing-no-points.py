from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = sorted([x for x, y in points])  # Extract and sort x-coordinates
        max_width = max(x_coords[i] - x_coords[i - 1] for i in range(1, len(x_coords)))
        return max_width
