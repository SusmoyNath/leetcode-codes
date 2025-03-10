from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = Counter(s)  # Count occurrences of each character
        stack = []  # Monotonic stack to store the result
        seen = set()  # Set to track added characters
        
        for char in s:
            char_count[char] -= 1  # Decrease count since we're processing it
            
            if char in seen:
                continue  # Skip if already in stack
            
            # Maintain lexicographic order: Remove elements that are larger & appear later
            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                seen.remove(stack.pop())  # Remove from set
            
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)  # Convert stack to string