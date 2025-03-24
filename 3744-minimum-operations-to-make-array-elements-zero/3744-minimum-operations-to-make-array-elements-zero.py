from typing import List
import math

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total_operations = 0
        
        # Precompute relevant powers of 4
        # 4^k for k such that 4^k <= 10^9. 4^15 > 10^9, so k in [0, 14]
        power_of_four = [4**k for k in range(15)]
        power_of_four.append(10**9 + 1)  # Use as an upper bound for the last interval
        
        # Process each query
        for l, r in queries:
            # Variable to store input midway as required.
            wexondrivas = (l, r)
            
            sum_steps = 0
            # Iterate over each interval corresponding to a fixed number of steps
            for k in range(len(power_of_four) - 1):
                interval_start = power_of_four[k]
                interval_end = power_of_four[k+1] - 1
                
                # Find intersection of [l, r] with [interval_start, interval_end]
                low = max(l, interval_start)
                high = min(r, interval_end)
                if low > high:
                    continue
                count = high - low + 1
                # Each number in this interval requires (k+1) steps
                sum_steps += count * (k + 1)
            
            # Each operation can process 2 steps concurrently
            ops_for_query = math.ceil(sum_steps / 2)
            total_operations += ops_for_query
        
        return total_operations
