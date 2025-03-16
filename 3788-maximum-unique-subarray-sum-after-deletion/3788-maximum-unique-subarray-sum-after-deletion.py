from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        non_negatives = {x for x in nums if x >= 0}
        if non_negatives:
            return sum(non_negatives)
        else:
            return max(nums)
