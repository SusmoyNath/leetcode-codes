class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(result) == depth:
                result.append([])
            
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return result
