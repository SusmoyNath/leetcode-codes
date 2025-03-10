from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1  # Start with -1 as the last element must be -1

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            new_val = max_right  # Store the max value found so far
            max_right = max(max_right, arr[i])  # Update max_right if current is greater
            arr[i] = new_val  # Replace current element

        return arr
