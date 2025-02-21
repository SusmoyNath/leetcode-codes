class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.values = set()  # Store all valid node values
        self.recover_tree(root, 0)

    def recover_tree(self, node, value):
        if not node:
            return
        node.val = value  # Set the correct value
        self.values.add(value)  # Store it in the set
        
        # Recursively fix left and right children
        self.recover_tree(node.left, 2 * value + 1)
        self.recover_tree(node.right, 2 * value + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values  # O(1) lookup time
