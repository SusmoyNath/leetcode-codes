class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If we find the target at mid, return True
            if nums[mid] == target:
                return True
            
            # If we can't decide which side is sorted due to duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return False
