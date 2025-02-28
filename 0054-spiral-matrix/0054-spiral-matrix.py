from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Move from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Move from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left

            # Move from right to left (if there's still a row remaining)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up

            # Move from bottom to top (if there's still a column remaining)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right

        return result
