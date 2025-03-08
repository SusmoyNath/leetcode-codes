from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)  # Insert a zero at position i
                arr.pop()  # Remove the last element to maintain array size
                i += 1  # Skip the next element to avoid duplicating more than needed
            i += 1  # Move to the next element