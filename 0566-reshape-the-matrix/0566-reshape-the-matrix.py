class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat  # Return original if reshape isn't possible

        flat = [num for row in mat for num in row]  # Flatten matrix
        return [flat[i * c:(i + 1) * c] for i in range(r)]  # Create reshaped matrix
