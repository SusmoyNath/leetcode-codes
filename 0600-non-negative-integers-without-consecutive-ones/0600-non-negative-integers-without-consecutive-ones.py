class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [0] * 31  # Store Fibonacci-like values up to 30 bits
        fib[0], fib[1] = 1, 2  # Base cases
        for i in range(2, 30):  # Precompute up to 30-bit numbers
            fib[i] = fib[i-1] + fib[i-2]
        
        prev_bit = 0  # Track previous bit
        result = 0  # Final count
        for i in range(29, -1, -1):  # Iterate from highest bit (29) to lowest
            if (n & (1 << i)):  # If bit i is set in n
                result += fib[i]  # Add valid numbers with (i-1) bits
                if prev_bit == 1:  # Consecutive ones detected â stop
                    return result
                prev_bit = 1  # Mark current bit as 1
            else:
                prev_bit = 0  # Mark current bit as 0
        
        return result + 1  # Include n itself if valid
