from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to use two-pointer approach
        closest_sum = float('inf')  # Initialize with infinity
        n = len(nums)

        for i in range(n - 2):  # Iterate until the third-last element
            left, right = i + 1, n - 1  # Two pointers

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if this total is closer to target
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total

                if total < target:
                    left += 1  # Increase sum by moving left pointer
                elif total > target:
                    right -= 1  # Decrease sum by moving right pointer
                else:
                    return total  # Exact match found, return immediately

        return closest_sum
