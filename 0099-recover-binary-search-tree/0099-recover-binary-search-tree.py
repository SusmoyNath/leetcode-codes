class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = second = prev = None
        current = root
        
        while current:
            if current.left is None:
                # Process current node
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                # Find the inorder predecessor
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right
                
                if pred.right is None:
                    pred.right = current  # Create temporary thread
                    current = current.left
                else:
                    pred.right = None  # Remove thread
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
        
        # Swap the values of the two nodes
        first.val, second.val = second.val, first.val
