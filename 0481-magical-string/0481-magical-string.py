class Solution(object):
    def magicalString(self, n):
        if n <= 0:
            return 0
        if n <= 3:
            return 1  # "122" has only one '1'

        s = [1, 2, 2]  # Initial sequence
        i = 2  # Pointer to control appending frequency
        next_num = 1  # We start appending '1'

        while len(s) < n:
            s.extend([next_num] * s[i])  # Append next_num, s[i] times
            next_num = 3 - next_num  # Alternate between 1 and 2
            i += 1  # Move to next index

        return s[:n].count(1)  # Count '1's in first n elements
