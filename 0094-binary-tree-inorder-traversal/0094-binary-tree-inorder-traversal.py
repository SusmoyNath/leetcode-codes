class Solution(object):
    def inorderTraversal(self, root):
        result, stack, current = [], [], root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
