from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def compare(x, y):
            return (y + x > x + y) - (y + x < x + y)  # Custom sorting logic

        nums = list(map(str, nums))  # Convert numbers to strings
        nums.sort(key=cmp_to_key(compare))  # Sort based on custom comparator

        result = ''.join(nums)  # Join sorted numbers into a single string
        return '0' if result[0] == '0' else result  # Handle cases like ["0", "0"]
