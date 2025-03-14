from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0  # Count of missing numbers
        num = 1      # Start from 1
        index = 0    # Pointer for arr
        
        while missing < k:
            if index < len(arr) and arr[index] == num:
                index += 1  # Move to the next element in arr
            else:
                missing += 1  # Count a missing number
                if missing == k:
                    return num  # Return when we reach k-th missing number
            num += 1  # Check the next number
