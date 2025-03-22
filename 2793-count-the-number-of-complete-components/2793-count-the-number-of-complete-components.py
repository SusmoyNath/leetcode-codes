from collections import defaultdict, deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_count = 0
        
        # Step 2: BFS to find connected components
        def bfs(node):
            queue = deque([node])
            component = set()
            edge_count = 0
            
            while queue:
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                component.add(cur)
                for neighbor in graph[cur]:
                    edge_count += 1
                    if neighbor not in visited:
                        queue.append(neighbor)
            
            # Step 3: Check if the component is complete
            m = len(component)
            expected_edges = m * (m - 1)
            return (edge_count // 2) == (expected_edges // 2)
        
        for i in range(n):
            if i not in visited:
                if bfs(i):
                    complete_count += 1
        
        return complete_count
