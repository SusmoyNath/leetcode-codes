class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # To simulate 32-bit integer
        INT_MAX = 0x7FFFFFFF  # Max positive integer (2^31 - 1)

        while b != 0:
            temp = (a & b) << 1  # Compute carry
            a = (a ^ b) & MASK   # Sum without carry
            b = temp & MASK       # Only keep 32-bit part of carry

        # If `a` is negative (exceeds 2^31), convert it to a signed integer
        return a if a <= INT_MAX else ~(a ^ MASK)
