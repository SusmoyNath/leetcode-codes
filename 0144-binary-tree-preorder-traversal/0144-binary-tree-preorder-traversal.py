class Solution(object):
    def preorderTraversal(self, root):
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
