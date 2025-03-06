class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])  # Rows and Columns
        result = [[0] * m for _ in range(n)]  # Create empty transposed matrix
        
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]  # Swap row and column indices
                
        return result
