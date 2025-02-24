class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  # Base index to compute valid lengths
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop last '(' index
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)  # Mark new base if empty

        return max_length
