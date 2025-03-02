class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        sum_nums = sum(nums)  # Sum of given numbers
        sum_set = sum(set(nums))  # Sum of unique numbers
        sum_n = n * (n + 1) // 2  # Sum of first N natural numbers

        duplicate = sum_nums - sum_set
        missing = sum_n - sum_set
        
        return [duplicate, missing]
