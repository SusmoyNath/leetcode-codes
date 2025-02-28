class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case explicitly
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamp to 32-bit integer max
        
        # Track the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple
            dividend -= temp
            quotient += multiple
        
        # Apply sign and return clamped result
        return -quotient if negative else quotient
