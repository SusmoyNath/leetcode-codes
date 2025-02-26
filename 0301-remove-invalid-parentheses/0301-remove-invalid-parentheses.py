from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def count_misplaced(s):
            left_to_remove, right_to_remove = 0, 0
            for char in s:
                if char == '(':
                    left_to_remove += 1
                elif char == ')':
                    if left_to_remove > 0:
                        left_to_remove -= 1
                    else:
                        right_to_remove += 1
            return left_to_remove, right_to_remove
        
        def backtrack(index, left_count, right_count, left_to_remove, right_to_remove, path):
            if index == len(s):
                if left_to_remove == 0 and right_to_remove == 0:
                    result.add("".join(path))
                return
            
            char = s[index]
            
            # Option 1: Remove invalid '(' or ')'
            if char == '(' and left_to_remove > 0:
                backtrack(index + 1, left_count, right_count, left_to_remove - 1, right_to_remove, path)
            if char == ')' and right_to_remove > 0:
                backtrack(index + 1, left_count, right_count, left_to_remove, right_to_remove - 1, path)
            
            # Option 2: Keep the current character
            path.append(char)
            if char == '(':
                backtrack(index + 1, left_count + 1, right_count, left_to_remove, right_to_remove, path)
            elif char == ')':
                if left_count > right_count:
                    backtrack(index + 1, left_count, right_count + 1, left_to_remove, right_to_remove, path)
            else:
                backtrack(index + 1, left_count, right_count, left_to_remove, right_to_remove, path)
            path.pop()  # Backtrack
            
        # Step 1: Find min '(' and ')' to remove
        left_to_remove, right_to_remove = count_misplaced(s)
        
        # Step 2: Backtracking with pruning
        result = set()
        backtrack(0, 0, 0, left_to_remove, right_to_remove, [])
        
        return list(result)
