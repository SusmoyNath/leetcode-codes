from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Single node case
        
        # Step 1: Build adjacency list
        adj = {i: set() for i in range(n)}
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        # Step 2: Find all leaf nodes (nodes with only one neighbor)
        leaves = deque([node for node in adj if len(adj[node]) == 1])
        
        # Step 3: Trim leaves level by level until 1 or 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Remove leaf from its neighbor
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                # If neighbor becomes a leaf, add it to the queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)  # The remaining nodes are MHT roots