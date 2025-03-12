from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []

        # Initialize the heap with (sum, index1, index2)
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # Extract k smallest pairs
        while k > 0 and min_heap:
            sum_val, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            
            # If there are more elements in nums2, push next pair
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result
