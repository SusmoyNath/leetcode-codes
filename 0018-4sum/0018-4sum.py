from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array
        n = len(nums)
        res = []

        for i in range(n - 3):  # First number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            for j in range(i + 1, n - 2):  # Second number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue

                left, right = j + 1, n - 1  # Two-pointer approach

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif four_sum < target:
                        left += 1  # Increase sum
                    else:
                        right -= 1  # Decrease sum

        return res
