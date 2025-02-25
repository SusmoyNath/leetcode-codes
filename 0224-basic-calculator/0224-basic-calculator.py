class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to handle parentheses
        num = 0  # Current number
        result = 0  # Current computed result
        sign = 1  # Current sign (1 for positive, -1 for negative)

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit numbers
            elif char == '+':
                result += sign * num  # Apply previous sign
                num = 0  # Reset num
                sign = 1  # Set sign for next number
            elif char == '-':
                result += sign * num  # Apply previous sign
                num = 0  # Reset num
                sign = -1  # Set sign for next number
            elif char == '(':
                stack.append(result)  # Save current result
                stack.append(sign)  # Save current sign
                result = 0  # Reset result inside parentheses
                sign = 1  # Reset sign inside parentheses
            elif char == ')':
                result += sign * num  # Apply last number before closing parenthesis
                num = 0  # Reset num
                result *= stack.pop()  # Multiply by sign before parenthesis
                result += stack.pop()  # Add result before parenthesis
            # Ignore spaces

        return result + (sign * num)  # Include last pending number
