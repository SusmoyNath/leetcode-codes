class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0  # Current depth
        max_depth = 0  # Maximum depth encountered

        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)  # Update max depth
            elif char == ')':
                depth -= 1  # Close a parenthesis, reduce depth
        
        return max_depth
