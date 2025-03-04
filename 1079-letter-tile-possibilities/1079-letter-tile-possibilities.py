from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        def backtrack(counter):
            total = 0
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    total += 1 + backtrack(counter)
                    counter[char] += 1
            return total
        
        return backtrack(Counter(tiles))
