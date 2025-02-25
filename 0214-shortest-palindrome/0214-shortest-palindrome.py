class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s
        
        # Step 1: Create new string with a delimiter
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        
        # Step 2: Compute KMP LPS array
        def computeLPS(pattern):
            lps = [0] * len(pattern)
            j = 0  # length of previous longest prefix suffix
            
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            
            return lps
        
        lps = computeLPS(new_s)
        longest_palindromic_prefix = lps[-1]
        
        # Step 3: Add the reversed suffix to the beginning
        suffix = s[longest_palindromic_prefix:]
        return suffix[::-1] + s
