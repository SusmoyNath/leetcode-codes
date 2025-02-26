class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using DFS (Preorder Traversal).
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return "null"
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree using DFS (Preorder Traversal).
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = iter(data.split(","))  # Use iterator to avoid list index tracking overhead
        
        def dfs():
            val = next(nodes)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
