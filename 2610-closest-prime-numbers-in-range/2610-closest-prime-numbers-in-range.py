import math

class Solution:
    def closestPrimes(self, left: int, right: int):
        if right < 2:
            return [-1, -1]  # No primes exist below 2

        # Step 1: Find all small primes up to sqrt(right) using Sieve of Eratosthenes
        limit = int(math.sqrt(right)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        small_primes = [i for i in range(2, limit + 1) if is_prime[i]]

        # Step 2: Use Segmented Sieve to mark primes in range [left, right]
        is_prime_range = [True] * (right - left + 1)
        if left == 1:
            is_prime_range[0] = False  # 1 is not a prime
        
        for p in small_primes:
            start = max(p * p, (left + p - 1) // p * p)
            for j in range(start, right + 1, p):
                is_prime_range[j - left] = False

        # Step 3: Collect primes in the range and find the closest pair
        primes = [i + left for i in range(right - left + 1) if is_prime_range[i]]

        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        ans = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap < min_gap:
                min_gap = gap
                ans = [primes[i - 1], primes[i]]

        return ans

# Example Usage:
sol = Solution()
print(sol.closestPrimes(10, 19))  # Output: [11, 13]
print(sol.closestPrimes(4, 6))    # Output: [-1, -1]