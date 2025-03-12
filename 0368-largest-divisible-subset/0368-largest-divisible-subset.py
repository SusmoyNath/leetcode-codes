from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()  # Sort to ensure divisibility condition is met naturally
        n = len(nums)
        dp = [1] * n  # Stores the length of the largest subset ending at index i
        parent = [-1] * n  # To track elements in the subset

        max_size = 0
        max_index = 0

        # Build dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Reconstruct the largest subset
        subset = []
        while max_index != -1:
            subset.append(nums[max_index])
            max_index = parent[max_index]

        return subset[::-1]  # Reverse to get the correct order
