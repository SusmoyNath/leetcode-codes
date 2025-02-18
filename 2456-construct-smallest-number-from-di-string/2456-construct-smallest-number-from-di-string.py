class Solution(object):
    def smallestNumber(self, pattern):
        stack, result = [], []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        return ''.join(result)
