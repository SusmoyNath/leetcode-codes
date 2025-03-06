import re

class Solution:
    def isValid(self, code: str) -> bool:
        tag_stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and not tag_stack:  # Outermost tag must enclose everything
                return False
            
            if code.startswith("<![CDATA[", i):  # Handle CDATA
                j = i + 9  # Move past "<![CDATA["
                i = code.find("]]>", j)
                if i == -1:  # CDATA must be properly closed
                    return False
                i += 3  # Move past "]]>"
            
            elif code.startswith("</", i):  # Handle closing tag
                j = i + 2  # Move past "</"
                k = code.find(">", j)
                if k == -1:
                    return False
                
                tag_name = code[j:k]
                if not tag_stack or tag_stack[-1] != tag_name:
                    return False  # Must match the last opened tag
                
                tag_stack.pop()
                i = k + 1  # Move past ">"
            
            elif code.startswith("<", i):  # Handle opening tag
                j = i + 1  # Move past "<"
                k = code.find(">", j)
                if k == -1:
                    return False
                
                tag_name = code[j:k]
                if not (1 <= len(tag_name) <= 9 and tag_name.isupper() and tag_name.isalpha()):
                    return False  # Invalid tag name (must be A-Z only, no '<', ' ' etc.)
                
                tag_stack.append(tag_name)
                i = k + 1  # Move past ">"
            
            else:  # Normal text, just move forward
                i += 1
        
        return not tag_stack  # Must be empty at the end (all tags closed)
