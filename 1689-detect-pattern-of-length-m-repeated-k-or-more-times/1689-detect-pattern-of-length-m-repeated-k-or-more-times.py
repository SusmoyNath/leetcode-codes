from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m * k + 1):  # Ensure enough space for k repetitions
            pattern = arr[i:i+m]  # Extract the pattern of length `m`
            count = 1  # Count starts at 1 (since we already have `pattern` once)

            # Check the next `k-1` occurrences of this pattern
            for j in range(i + m, i + m * k, m):
                if arr[j:j+m] == pattern:
                    count += 1
                else:
                    break  # Stop if the pattern does not match

            if count >= k:  # If pattern appears `k` times
                return True

        return False
