from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()  # Sort the array
        diff = arr[1] - arr[0]  # Calculate common difference
        
        # Check if all consecutive elements have the same difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        
        return True
