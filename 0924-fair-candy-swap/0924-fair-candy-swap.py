from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        delta = (sumAlice - sumBob) // 2  # Integer division since sumAlice - sumBob is always even
        
        bobSet = set(bobSizes)  # Convert Bob's list to a set for O(1) lookup
        
        for a in aliceSizes:
            b = a - delta  # The value Bob needs to give
            if b in bobSet:
                return [a, b]  # Valid swap found
