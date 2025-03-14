from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # Track how deep we are in the folder structure
        
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1  # Move up one level
            elif log != "./":
                depth += 1  # Move to a child folder
        
        return depth
