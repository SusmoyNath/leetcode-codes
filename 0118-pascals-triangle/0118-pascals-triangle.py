class Solution(object):
    def generate(self, numRows):
        result = [[1]]
        for i in range(1, numRows):
            row = [1] + [result[i-1][j-1] + result[i-1][j] for j in range(1, i)] + [1]
            result.append(row)
        return result
