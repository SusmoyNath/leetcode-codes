from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()  # Sort the array
        n = len(arr)
        remove_count = n // 20  # 5% of the elements to remove from each end
        
        trimmed_arr = arr[remove_count:-remove_count]  # Slice the array
        return sum(trimmed_arr) / len(trimmed_arr)  # Compute the mean
