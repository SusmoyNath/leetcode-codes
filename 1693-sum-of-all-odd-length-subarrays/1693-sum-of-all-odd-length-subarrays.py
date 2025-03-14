from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            left = i + 1
            right = n - i
            count = (left * right + 1) // 2  # Count of times arr[i] appears in odd-length subarrays
            total_sum += arr[i] * count
            
        return total_sum
