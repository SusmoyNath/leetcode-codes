from heapq import heappush, heappop
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]  # Min-heap initialized with 1 (first super ugly number)
        seen = set(heap)  # Set to avoid duplicates
        
        for _ in range(n):  # Find the nth super ugly number
            smallest = heappop(heap)  # Get the smallest super ugly number
            
            for prime in primes:  # Generate new numbers
                new_ugly = smallest * prime  # Multiply with each prime
                if new_ugly not in seen:
                    heappush(heap, new_ugly)
                    seen.add(new_ugly)
        
        return smallest  # The nth super ugly number
