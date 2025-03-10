from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()  # Sort arr2 for efficient searching
        count = 0
        
        for num in arr1:
            idx = bisect.bisect_left(arr2, num)  # Find the insertion position
            
            # Check left neighbor
            if idx > 0 and abs(num - arr2[idx - 1]) <= d:
                continue
            
            # Check right neighbor
            if idx < len(arr2) and abs(num - arr2[idx]) <= d:
                continue
            
            count += 1  # If neither neighbor satisfies |num - arr2[j]| â¤ d
        
        return count
