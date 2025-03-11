class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}  # Track counts of 'a', 'b', 'c'
        left = 0  # Left pointer
        result = 0  # Store count of valid substrings
        
        for right in range(len(s)):  # Expand the right pointer
            count[s[right]] += 1  # Include s[right] in window
            
            # Move left pointer while the window is valid
            while all(count[c] > 0 for c in 'abc'):
                result += len(s) - right  # All substrings ending at right are valid
                count[s[left]] -= 1  # Shrink window
                left += 1  # Move left pointer
        
        return result