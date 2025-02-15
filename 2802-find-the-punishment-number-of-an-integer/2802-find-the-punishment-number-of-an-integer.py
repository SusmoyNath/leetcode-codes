class Solution(object):
    def punishmentNumber(self, n):
        def canPartition(s, target, index):
            if index == len(s):
                return target == 0
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if num > target:
                    break
                if canPartition(s, target - num, i + 1):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if canPartition(square_str, i, 0):
                total += i * i
        
        return total
