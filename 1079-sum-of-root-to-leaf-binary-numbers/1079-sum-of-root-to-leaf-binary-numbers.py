class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = (current_sum << 1) | node.val  # Shift left and add current node value
            
            if not node.left and not node.right:  # If it's a leaf node, return the computed number
                return current_sum
            
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)  # Recur for left and right children
        
        return dfs(root, 0)
