class Solution(object):
    def findDifferentBinaryString(self, nums):
        num_set = set(nums)
        n = len(nums)
        for i in range(2 ** n):
            binary_str = format(i, '0' + str(n) + 'b') 
            if binary_str not in num_set:
                return binary_str