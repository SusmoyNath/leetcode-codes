from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort to bring negative numbers to the front
        
        # Flip negative numbers while k > 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        # If k is still positive and odd, flip the smallest number
        if k % 2 == 1:
            nums.sort()  # Re-sort to find the smallest element
            nums[0] = -nums[0]
        
        return sum(nums)
