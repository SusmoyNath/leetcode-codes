from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        
        # If total sum is not divisible by 3, we cannot split into 3 equal parts
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3  # Each partition should sum to this
        count, current_sum = 0, 0
        
        for i in range(len(arr) - 1):  # Ensure last partition is non-empty
            current_sum += arr[i]
            if current_sum == target:
                count += 1
                current_sum = 0  # Reset to find the next partition
                
                if count == 2:  # If we found two partitions, the rest must form the third
                    return True
        
        return False  # If we didn't find two partitions, return False
