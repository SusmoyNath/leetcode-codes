from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Iterate from highest freq
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
