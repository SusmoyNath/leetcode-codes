class Solution(object):
    def findComplement(self, num):
        # Step 1: Find the bit length of num
        bit_length = num.bit_length()

        # Step 2: Create a mask with all 1s of the same length as num
        mask = (1 << bit_length) - 1  # Example: If num = 5 (101), mask = 111 (7)

        # Step 3: Compute the complement using XOR
        return num ^ mask
