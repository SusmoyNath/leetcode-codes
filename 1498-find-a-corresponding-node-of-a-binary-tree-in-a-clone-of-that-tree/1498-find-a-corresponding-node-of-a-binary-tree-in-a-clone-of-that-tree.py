class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Base Case: If original is None, return None
        if not original:
            return None
        
        # If we found the target node in the original tree
        if original == target:
            return cloned  # Return the corresponding node in cloned tree
        
        # Search in the left subtree
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result  # If found, return the result
        
        # Search in the right subtree
        return self.getTargetCopy(original.right, cloned.right, target)
