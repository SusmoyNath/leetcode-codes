from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i-1][0])
            y_diff = abs(points[i][1] - points[i-1][1])
            time += max(x_diff, y_diff)  # Move diagonally as much as possible, then straight
        return time
