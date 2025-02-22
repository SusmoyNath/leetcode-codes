class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0  # Stores maximum consecutive 1s
        current_count = 0  # Tracks current streak of 1s
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0  # Reset streak if 0 is encountered
        
        return max_count