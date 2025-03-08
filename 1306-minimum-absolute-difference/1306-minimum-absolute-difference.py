from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Step 1: Sort the array
        min_diff = float('inf')
        result = []

        # Step 2: Find the minimum absolute difference
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]  # Reset list with new min difference pairs
            elif diff == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result