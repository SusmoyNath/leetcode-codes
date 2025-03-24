from typing import List
from collections import defaultdict

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        
        # Function to find the number of common elements
        def intersect(a, b):
            return len(set(a) & set(b))
        
        # Build adjacency list
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # DFS to count connected components
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        components = 0
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        
        return components
