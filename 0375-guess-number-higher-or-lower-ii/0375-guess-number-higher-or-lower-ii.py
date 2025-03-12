class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill DP table
        for length in range(2, n + 1):  # length of range
            for i in range(1, n - length + 2):  # start of range
                j = i + length - 1  # end of range
                dp[i][j] = float('inf')

                for k in range(i, j + 1):
                    cost = k + max(dp[i][k-1] if k > i else 0, dp[k+1][j] if k < j else 0)
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]
