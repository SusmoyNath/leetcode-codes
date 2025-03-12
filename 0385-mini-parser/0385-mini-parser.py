class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):  
            return NestedInteger(int(s))  # Single integer case

        stack = []
        num = None
        negative = False  # Flag for negative numbers

        for i, char in enumerate(s):
            if char == '[':
                stack.append(NestedInteger())  # Start a new list
            elif char == '-':
                negative = True  # Next number will be negative
            elif char.isdigit():
                if num is None:
                    num = int(char)
                else:
                    num = num * 10 + int(char)
            elif char == ',' or char == ']':
                if num is not None:  # If we just finished reading a number
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                    num = None
                    negative = False  # Reset negative flag

                if char == ']' and len(stack) > 1:  # Merge nested list
                    ni = stack.pop()
                    stack[-1].add(ni)
                    
        return stack[0]  # The final NestedInteger object
