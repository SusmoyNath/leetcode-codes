class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, path, result):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            path.pop()

        result = []
        dfs(root, [], result)
        return result