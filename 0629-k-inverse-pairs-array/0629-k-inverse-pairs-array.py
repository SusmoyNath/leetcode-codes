class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: One way to arrange an empty array
        
        for i in range(1, n + 1):
            prefix_sum = [0] * (k + 1)
            prefix_sum[0] = dp[i - 1][0]
            
            for j in range(1, k + 1):
                prefix_sum[j] = (prefix_sum[j - 1] + dp[i - 1][j]) % MOD
            
            for j in range(k + 1):
                dp[i][j] = prefix_sum[j]
                if j >= i:
                    dp[i][j] = (dp[i][j] - prefix_sum[j - i]) % MOD
        
        return dp[n][k]

# Example usage:
sol = Solution()
print(sol.kInversePairs(3, 0))  # Output: 1
print(sol.kInversePairs(3, 1))  # Output: 2