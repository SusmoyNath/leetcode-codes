from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            return
        
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)  # Segment tree with size 2 * n
        self.buildTree(nums)

    def buildTree(self, nums: List[int]):
        # Build the tree from the input array
        for i in range(self.n):  
            self.tree[self.n + i] = nums[i]  # Fill leaves
        
        for i in range(self.n - 1, 0, -1):  
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]  # Build parent nodes

    def update(self, index: int, val: int) -> None:
        pos = index + self.n  # Locate the leaf node
        self.tree[pos] = val  # Update value
        
        # Update parent nodes
        while pos > 1:
            pos //= 2  # Move to parent
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n  # Convert to tree index
        sum_ = 0
        
        while l <= r:
            if l % 2 == 1:  # If l is a right child
                sum_ += self.tree[l]
                l += 1
            
            if r % 2 == 0:  # If r is a left child
                sum_ += self.tree[r]
                r -= 1
            
            l //= 2  # Move up
            r //= 2
        
        return sum_
