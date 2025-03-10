from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        mid = (n - 1) // 2  # Middle index (for smaller numbers)
        
        # Create a copy of the sorted array
        sorted_nums = nums[:]
        
        # Step 2: Fill odd indices with larger values
        j = n - 1  # Largest elements
        for i in range(1, n, 2):
            nums[i] = sorted_nums[j]
            j -= 1
        
        # Step 3: Fill even indices with smaller values
        for i in range(0, n, 2):
            nums[i] = sorted_nums[mid]
            mid -= 1
