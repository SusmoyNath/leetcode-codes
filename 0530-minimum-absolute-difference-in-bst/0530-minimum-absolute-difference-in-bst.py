class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            values.append(node.val)
            in_order_traversal(node.right)
        
        values = []
        in_order_traversal(root)
        return min(abs(values[i] - values[i - 1]) for i in range(1, len(values)))
