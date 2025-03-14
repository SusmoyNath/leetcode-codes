class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)  # Convert string to list for mutability
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                # Pick a character that is not the same as adjacent characters
                for ch in 'abc':
                    if (i > 0 and s[i - 1] == ch) or (i < n - 1 and s[i + 1] == ch):
                        continue
                    s[i] = ch
                    break
        
        return "".join(s)  # Convert back to string
