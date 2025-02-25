from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []
        
        result = []
        dq = deque()  # Stores indices of useful elements
        
        for i in range(len(nums)):
            # Remove elements out of window bounds (leftmost)
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Maintain decreasing order in deque (pop smaller elements)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add current element index to deque
            dq.append(i)
            
            # Store the maximum of the current window
            if i >= k - 1:
                result.append(nums[dq[0]])  # Front of deque is max
            
        return result
