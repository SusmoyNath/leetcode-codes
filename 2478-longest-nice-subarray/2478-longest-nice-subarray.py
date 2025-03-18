from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0  # Left pointer
        used_bits = 0  # Tracks bits used in the window
        max_length = 0  # Stores the maximum length of the nice subarray

        for r in range(len(nums)):  # Right pointer moves forward
            # Shrink window if there's a bitwise conflict
            while (used_bits & nums[r]) != 0:
                used_bits ^= nums[l]  # Remove nums[l] from the window
                l += 1  # Move left pointer

            # Add nums[r] to the window
            used_bits |= nums[r]
            max_length = max(max_length, r - l + 1)  # Update max length

        return max_length
