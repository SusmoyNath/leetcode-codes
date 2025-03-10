from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        char_count = Counter(s)
        result = []
        
        unique_chars = sorted(char_count.keys())
        
        while len(result) < len(s):
            for ch in unique_chars:
                if char_count[ch] > 0:
                    result.append(ch)
                    char_count[ch] -= 1
            
            for ch in reversed(unique_chars):
                if char_count[ch] > 0:
                    result.append(ch)
                    char_count[ch] -= 1
        
        return "".join(result)
