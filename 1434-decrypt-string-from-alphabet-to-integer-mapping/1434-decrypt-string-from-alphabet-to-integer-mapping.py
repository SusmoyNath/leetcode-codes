class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        result = []
        
        while i < len(s):
            # Check if we have a two-digit number followed by '#'
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(int(s[i:i+2]) + 96))  # Convert '10' - '26' to 'j' - 'z'
                i += 3  # Move past the processed part
            else:
                result.append(chr(int(s[i]) + 96))  # Convert '1' - '9' to 'a' - 'i'
                i += 1
        
        return "".join(result)