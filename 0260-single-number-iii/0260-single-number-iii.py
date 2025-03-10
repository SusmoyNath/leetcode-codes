from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers
        xor = 0
        for num in nums:
            xor ^= num
        
        # Step 2: Find rightmost set bit (difference bit)
        diff_bit = xor & -xor  # This isolates the lowest set bit
        
        # Step 3: Separate into two groups and XOR each group
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num  # XOR numbers where the bit is set
            else:
                num2 ^= num  # XOR numbers where the bit is not set

        return [num1, num2]