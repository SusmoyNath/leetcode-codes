class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove adjacent duplicate
            else:
                stack.append(char)  # Add character to stack
        
        return "".join(stack)  # Convert list back to string
