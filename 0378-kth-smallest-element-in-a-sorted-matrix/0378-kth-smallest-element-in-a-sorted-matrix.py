from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def countLessEqual(mid):
            """Returns count of elements <= mid in the matrix."""
            count, row, col = 0, n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1  # All elements above are <= mid
                    col += 1
                else:
                    row -= 1
            return count
        
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
