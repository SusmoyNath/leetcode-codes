class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(maxSum):
            subarrays = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > maxSum:
                    subarrays += 1
                    curr_sum = num  # Start a new subarray
                    if subarrays > k:
                        return False
                else:
                    curr_sum += num
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid  # Try a smaller max sum
            else:
                left = mid + 1  # Increase allowed sum
        return left
