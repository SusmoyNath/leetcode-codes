from collections import Counter

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        
        # Dictionary to store the frequency of values
        count = Counter()
        
        # In-order traversal to count occurrences
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            count[node.val] += 1
            inorder(node.right)
        
        inorder(root)  # Perform the in-order traversal
        
        # Find the maximum frequency
        max_freq = max(count.values())
        
        # Collect all elements with the max frequency
        return [k for k, v in count.items() if v == max_freq]
