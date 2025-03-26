from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a single list
        arr = [num for row in grid for num in row]
        
        # Check if it's possible to make all elements the same
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1  # Not possible
        
        # Sort the array
        arr.sort()
        
        # Find the median
        median = arr[len(arr) // 2]
        
        # Compute operations to make all elements equal to median
        operations = sum(abs(num - median) // x for num in arr)
        
        return operations
