class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        result, start = [], nums[0]
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                result.append(str(start) if start == nums[i - 1] else str(start) + "->" + str(nums[i - 1]))
                if i < len(nums):
                    start = nums[i]
        return result
