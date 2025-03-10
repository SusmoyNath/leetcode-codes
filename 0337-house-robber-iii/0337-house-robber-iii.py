from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this, skip_this)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we must skip its direct children
            rob_this = node.val + left[1] + right[1]
            
            # If we skip this node, we take the max from its children
            skip_this = max(left) + max(right)
            
            return (rob_this, skip_this)
        
        return max(dfs(root))