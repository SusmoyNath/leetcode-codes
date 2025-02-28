from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer approach
        result = []
        n = len(nums)
        
        for i in range(n - 2):  # Iterate until the third-last element
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for 'i'
                continue
            
            left, right = i + 1, n - 1  # Two-pointer initialization
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Increase sum by moving left pointer
                else:
                    right -= 1  # Decrease sum by moving right pointer
        
        return result
