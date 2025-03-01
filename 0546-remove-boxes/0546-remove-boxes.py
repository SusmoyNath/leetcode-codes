from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        @lru_cache(None)  # Memoization
        def dp(l, r, k):
            if l > r:
                return 0
            
            # Extend the sequence of same-colored boxes
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            
            # Case 1: Remove the current group at `r`
            max_points = (k + 1) * (k + 1) + dp(l, r - 1, 0)
            
            # Case 2: Try merging a previous occurrence of the same color
            for m in range(l, r):
                if boxes[m] == boxes[r]:
                    max_points = max(max_points, dp(l, m, k + 1) + dp(m + 1, r - 1, 0))
            
            return max_points

        return dp(0, len(boxes) - 1, 0)
