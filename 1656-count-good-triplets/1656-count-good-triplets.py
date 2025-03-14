from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        
        # Iterate over j (middle element)
        for j in range(1, n - 1):
            valid_i = []  # Stores valid 'i' values where |arr[i] - arr[j]| <= a
            valid_k = []  # Stores valid 'k' values where |arr[k] - arr[j]| <= b
            
            # Find all valid i values for the current j
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    valid_i.append(arr[i])
            
            # Find all valid k values for the current j
            for k in range(j + 1, n):
                if abs(arr[k] - arr[j]) <= b:
                    valid_k.append(arr[k])
            
            # Count triplets where |arr[i] - arr[k]| <= c
            for x in valid_i:
                for y in valid_k:
                    if abs(x - y) <= c:
                        count += 1
        
        return count
