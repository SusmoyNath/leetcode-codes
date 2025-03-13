class Solution(object):
    def totalHammingDistance(self, nums):
        total_distance = 0
        n = len(nums)

        for bit in range(32):  # Since 0 <= nums[i] <= 10^9, max 32-bit integer
            count_ones = sum((num >> bit) & 1 for num in nums)
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        
        return total_distance
