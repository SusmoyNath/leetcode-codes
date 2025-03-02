class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]  # Create result matrix

        # Directions for 3x3 neighborhood
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),  (0, 0),  (0, 1), 
                      (1, -1),  (1, 0),  (1, 1)]

        for i in range(m):
            for j in range(n):
                total, count = 0, 0

                # Check all valid neighbors
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        total += img[ni][nj]
                        count += 1

                result[i][j] = total // count  # Floor division

        return result
