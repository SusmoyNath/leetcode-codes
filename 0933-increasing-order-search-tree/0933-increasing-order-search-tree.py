from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node):
            """ Perform in-order traversal and re-link nodes """
            if not node:
                return
            inorder_traversal(node.left)  # Left subtree
            node.left = None  # Remove left child
            self.curr.right = node  # Attach current node to right
            self.curr = node  # Move current pointer
            inorder_traversal(node.right)  # Right subtree

        dummy = TreeNode(-1)  # Dummy node to track the new tree
        self.curr = dummy
        inorder_traversal(root)

        return dummy.right  # The first real node is the new root
