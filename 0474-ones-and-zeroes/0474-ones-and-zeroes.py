class Solution(object):
    def findMaxForm(self, strs, m, n):
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Process each string
        for s in strs:
            zeroes = s.count('0')
            ones = s.count('1')
            
            # Traverse DP table from bottom-right to top-left to avoid overwriting
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)
        
        return dp[m][n]
