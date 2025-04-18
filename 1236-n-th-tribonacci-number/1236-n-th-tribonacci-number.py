class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        a, b, c = 0, 1, 1  # Initialize T0, T1, T2
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c  # Update values iteratively
        
        return c