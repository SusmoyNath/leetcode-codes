class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1  # Start from units place
        
        while factor <= n:
            high = n // (factor * 10)  # Digits left of current position
            curr = (n // factor) % 10  # Current digit
            low = n % factor  # Digits right of current position
            
            if curr == 0:
                count += high * factor
            elif curr == 1:
                count += high * factor + (low + 1)
            else:
                count += (high + 1) * factor
            
            factor *= 10  # Move to the next digit place
            
        return count
