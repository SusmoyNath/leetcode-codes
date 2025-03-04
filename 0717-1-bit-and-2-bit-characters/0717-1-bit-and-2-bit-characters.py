class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)
        
        while i < n - 1:  # Traverse until second-last index
            if bits[i] == 1:
                i += 2  # Skip two-bit character
            else:
                i += 1  # Move to next one-bit character
        
        return i == n - 1  # True if last character is one-bit
