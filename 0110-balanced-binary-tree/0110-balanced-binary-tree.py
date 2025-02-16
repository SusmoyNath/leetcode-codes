class Solution(object):
    def isBalanced(self, root):
        def checkHeight(node):
            if not node:
                return 0
            left = checkHeight(node.left)
            right = checkHeight(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        
        return checkHeight(root) != -1
