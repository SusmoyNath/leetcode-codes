class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Add the node to the result first
            for child in node.children:
                stack.append(child)  # Add children to the stack
        
        return result[::-1]  # Reverse the result to get postorder

# Example usage
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
solution = Solution()
result = solution.postorder(root)
print(result)  # Output: [5, 6, 3, 2, 4, 1]
