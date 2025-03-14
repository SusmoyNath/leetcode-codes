class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  # Remove bad adjacent pair
            else:
                stack.append(char)  # Keep the character
        
        return "".join(stack)
