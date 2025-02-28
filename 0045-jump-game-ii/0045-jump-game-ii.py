class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:  
            return 0  # No jumps needed if we start and end at the same position
        
        jumps, current_end, farthest = 0, 0, 0
        
        for i in range(len(nums) - 1):  # No need to check last element
            farthest = max(farthest, i + nums[i])  # Update max reach
            
            if i == current_end:  # End of current jump range
                jumps += 1
                current_end = farthest  # Move to the next range
                
                if current_end >= len(nums) - 1:  # If we reach the last index, return jumps
                    return jumps
        
        return jumps
