from collections import Counter

class Solution:
    def findLHS(self, nums):
        # Step 1: Count frequencies of each number
        count = Counter(nums)
        max_length = 0
        
        # Step 2: Check for each number x if x+1 exists and calculate the subsequence length
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
        
        return max_length
