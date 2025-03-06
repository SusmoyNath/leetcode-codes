class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getNextValidCharIndex(string, index):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return index
                index -= 1
            return index
        
        i, j = len(s) - 1, len(t) - 1
        
        while i >= 0 or j >= 0:
            i = getNextValidCharIndex(s, i)
            j = getNextValidCharIndex(t, j)
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j >= 0):  # One string is exhausted while the other is not
                return False
            
            i -= 1
            j -= 1
        
        return True
