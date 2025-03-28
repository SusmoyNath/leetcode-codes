from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        # Sort queries with their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        # Min-heap for BFS (value, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        # Result array
        results = [0] * len(queries)
        points = 0  # Total points collected
        prev_query = 0  # Track the last processed query

        for idx, query in sorted_queries:
            # Expand BFS until the grid values exceed the query
            while min_heap and min_heap[0][0] < query:
                value, r, c = heappop(min_heap)

                # Count this cell if it's visited for the first time
                points += 1

                # Explore 4 possible moves
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True

            results[idx] = points  # Store the result in the original order

        return results
