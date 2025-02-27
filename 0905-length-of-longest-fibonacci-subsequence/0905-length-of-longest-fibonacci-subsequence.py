from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(arr)}  # Map value to index
        n = len(arr)
        dp = {}
        max_len = 0

        for j in range(n):
            for i in range(j):
                expected = arr[j] - arr[i]  # Find the number to form Fibonacci sequence
                if expected < arr[i] and expected in index_map:
                    k = index_map[expected]  # Get index of expected number
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])

        return max_len if max_len >= 3 else 0  # Return 0 if no valid subsequence exists
