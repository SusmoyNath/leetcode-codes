class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]  # Convert to binary string
        max_gap = 0
        prev = -1  # Track previous '1' index
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if prev != -1:
                    max_gap = max(max_gap, i - prev)
                prev = i  # Update previous '1' index
        
        return max_gap
