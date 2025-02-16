class Solution(object):
    def majorityElement(self, nums):
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
