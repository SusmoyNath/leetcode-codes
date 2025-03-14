class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = [], []
        
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)
        
        # If the difference in count is more than 1, we cannot reformat
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        # Ensure we start with the larger group
        if len(letters) < len(digits):
            letters, digits = digits, letters
        
        # Interleave letters and digits
        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])
        
        # If letters are more, append the extra letter
        if len(letters) > len(digits):
            result.append(letters[-1])
        
        return "".join(result)
