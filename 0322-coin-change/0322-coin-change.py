from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize DP array with "infinity" (unreachable state)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Step 2: Iterate over all amounts up to "amount"
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Step 3: Return result (if "inf", return -1)
        return dp[amount] if dp[amount] != float('inf') else -1