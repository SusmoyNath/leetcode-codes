class Solution:
    def findMaxAverage(self, nums, k):
        # Compute the sum of the first k elements (initial window)
        max_sum = curr_sum = sum(nums[:k])
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]  # Add new element, remove old element
            max_sum = max(max_sum, curr_sum)  # Update max sum if needed
        
        # Return the maximum average
        return max_sum / k
