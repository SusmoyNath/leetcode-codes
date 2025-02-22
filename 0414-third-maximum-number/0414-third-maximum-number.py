class Solution(object):
    def thirdMax(self, nums):
        unique_nums = list(set(nums))  # Remove duplicates
        unique_nums.sort(reverse=True)  # Sort in descending order
        
        if len(unique_nums) >= 3:
            return unique_nums[2]  # Return third maximum
        return unique_nums[0]  # Return the maximum if third does not exist
