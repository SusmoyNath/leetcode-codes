from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Start with the root in the queue
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for _ in range(level_count):  # Process all nodes in the current level
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_sum / level_count)  # Store average of the level
        
        return result
