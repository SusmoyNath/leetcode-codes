class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            odd_palindrome = expandAroundCenter(i, i)
            even_palindrome = expandAroundCenter(i, i + 1)
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest
