import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        """ Initialize with the original array. """
        self.original = nums[:]  # Store the original array
        self.array = nums[:]      # Create a working copy

    def reset(self) -> List[int]:
        """ Reset to the original array. """
        self.array = self.original[:]  # Restore original order
        return self.array

    def shuffle(self) -> List[int]:
        """ Return a randomly shuffled array using Fisher-Yates Shuffle. """
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)  # Pick a random index from 0 to i
            self.array[i], self.array[j] = self.array[j], self.array[i]  # Swap
        return self.array
