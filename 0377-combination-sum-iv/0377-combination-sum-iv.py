from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case
        
        for i in range(1, target + 1):  # Compute dp[i] for all targets
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]
