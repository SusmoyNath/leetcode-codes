from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask_map = {}  # Dictionary to store max length for each unique bitmask
        
        # Step 1: Convert words into bitmasks and store max length per bitmask
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))  # Set bit for character
            bitmask_map[bitmask] = max(bitmask_map.get(bitmask, 0), len(word)) 
        
        # Step 2: Find max product of lengths of words with non-overlapping bitmasks
        max_product = 0
        bitmasks = list(bitmask_map.keys())
        
        for i in range(len(bitmasks)):
            for j in range(i + 1, len(bitmasks)):
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    max_product = max(max_product, bitmask_map[bitmasks[i]] * bitmask_map[bitmasks[j]])
        
        return max_product