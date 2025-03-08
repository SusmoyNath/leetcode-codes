class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0  # Keeps track of open '(' minus closed ')'

        for char in s:
            if char == '(':
                if balance > 0:  # Ignore the first '(' of a primitive sequence
                    result.append(char)
                balance += 1
            else:  # char == ')'
                balance -= 1
                if balance > 0:  # Ignore the last ')' of a primitive sequence
                    result.append(char)

        return "".join(result)
