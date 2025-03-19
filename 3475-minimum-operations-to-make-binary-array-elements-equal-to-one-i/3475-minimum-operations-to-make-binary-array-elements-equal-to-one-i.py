from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0  # Count of operations
        
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the next 3 elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1

        # Final check: If any `0` is left, return -1
        return ops if all(num == 1 for num in nums) else -1
