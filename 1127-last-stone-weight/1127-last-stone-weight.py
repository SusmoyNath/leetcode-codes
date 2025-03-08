import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones into a max heap by negating values (Python only has min heap)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Extract the two heaviest stones
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            # If they are not equal, push the difference back
            if x != y:
                heapq.heappush(max_heap, -(y - x))

        # Return the last remaining stone or 0 if none are left
        return -max_heap[0] if max_heap else 0
