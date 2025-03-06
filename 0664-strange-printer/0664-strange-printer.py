class Solution:
    def strangePrinter(self, s: str) -> int:
        # Remove consecutive duplicates
        s = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i - 1])
        n = len(s)
        
        # Edge case: if s is empty, return 0
        if n == 0:
            return 0
        
        # DP table
        dp = [[0] * n for _ in range(n)]
        
        # Base case: a single character needs exactly 1 turn
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table for substrings of increasing length
        for length in range(2, n + 1):  # Length of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # End index
                
                # Default case: Print separately
                dp[i][j] = 1 + dp[i + 1][j]
                
                # Try merging to minimize print turns
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:  # If matching char found, attempt merge
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))

        return dp[0][n - 1]
