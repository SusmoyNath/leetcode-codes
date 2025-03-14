class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')  # Count all ones in s
        left_zeros = 0
        right_ones = total_ones
        max_score = float('-inf')
        
        for i in range(len(s) - 1):  # Do not split at the last index
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1  # Remove the current '1' from right
            
            max_score = max(max_score, left_zeros + right_ones)
        
        return max_score
