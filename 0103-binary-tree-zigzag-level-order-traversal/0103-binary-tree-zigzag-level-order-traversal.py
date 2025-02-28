class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(result) == depth:
                result.append([])  # Create new list for the level
            
            if depth % 2 == 0:
                result[depth].append(node.val)  # Left to right
            else:
                result[depth].insert(0, node.val)  # Right to left
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return result
