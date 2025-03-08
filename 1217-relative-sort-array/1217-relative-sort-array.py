from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001  # Create a frequency array for numbers 0-1000
        for num in arr1:
            count[num] += 1  # Count occurrences of each number
        
        result = []
        
        # Add numbers from arr2 in the correct order
        for num in arr2:
            result.extend([num] * count[num])  # Append 'num' count[num] times
            count[num] = 0  # Mark as used
        
        # Append the remaining numbers in sorted order
        for num in range(1001):
            if count[num] > 0:
                result.extend([num] * count[num])  # Append remaining elements
        
        return result
