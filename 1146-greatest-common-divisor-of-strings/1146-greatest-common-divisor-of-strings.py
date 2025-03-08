from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the two strings can be constructed using a common substring
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd_length
        return str1[:gcd_length]
