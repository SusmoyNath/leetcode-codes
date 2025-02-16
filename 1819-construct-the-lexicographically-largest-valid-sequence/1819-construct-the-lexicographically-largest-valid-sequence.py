class Solution(object):
    def constructDistancedSequence(self, n):
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            if index == len(result):
                return True
            if result[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1 or (index + num < len(result) and result[index + num] == 0):
                    result[index] = num
                    if num > 1:
                        result[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    if num > 1:
                        result[index + num] = 0
                    used[num] = False
            return False

        backtrack(0)
        return result
