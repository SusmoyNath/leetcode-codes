from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Find the minimum value in each row
        row_min = {min(row) for row in matrix}
        
        # Find the maximum value in each column
        col_max = {max(col) for col in zip(*matrix)}
        
        # The lucky numbers are the intersection of these sets
        return list(row_min & col_max)
