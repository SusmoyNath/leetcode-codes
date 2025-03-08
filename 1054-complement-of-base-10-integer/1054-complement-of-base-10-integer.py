class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1  # Edge case: complement of 0 is 1

        bit_length = n.bit_length()  # Get number of bits in n
        mask = (1 << bit_length) - 1  # Create a bitmask with all bits set to 1

        return n ^ mask  # XOR with mask to flip bits
