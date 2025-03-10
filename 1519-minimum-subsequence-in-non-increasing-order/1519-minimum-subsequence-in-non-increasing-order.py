from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)  # Step 1: Sort in descending order
        total_sum = sum(nums)  # Compute the total sum of the array
        
        subseq_sum = 0
        subseq = []
        
        for num in nums:  # Step 2: Iterate through sorted nums
            subseq_sum += num
            subseq.append(num)
            if subseq_sum > total_sum - subseq_sum:  # Step 3: Check condition
                break
        
        return subseq  # Step 4: Return the valid subsequence
