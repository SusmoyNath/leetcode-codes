from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Function to count primes â¤ n
        def count_primes(n):
            if n < 2:
                return 0
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
            return sum(primes)
        
        prime_count = count_primes(n)
        non_prime_count = n - prime_count
        
        # Compute the result using factorial
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD