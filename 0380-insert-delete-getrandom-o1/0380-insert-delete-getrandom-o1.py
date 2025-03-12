import random

class RandomizedSet:
    def __init__(self):
        self.num_to_idx = {}  # {val: index}
        self.nums = []  # List to store values

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False
        self.num_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_idx:
            return False
        
        # Get index of element to remove
        idx_to_remove = self.num_to_idx[val]
        last_val = self.nums[-1]  # Get last element in list
        
        # Swap last element with the one to remove
        self.nums[idx_to_remove] = last_val
        self.num_to_idx[last_val] = idx_to_remove  # Update index in dict
        
        # Remove last element from list and dictionary
        self.nums.pop()
        del self.num_to_idx[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
