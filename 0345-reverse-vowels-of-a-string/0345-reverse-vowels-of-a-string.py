class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")  # Define vowel set for quick lookup
        s = list(s)  # Convert string to a list for mutability
        left, right = 0, len(s) - 1  # Two-pointer approach

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1  # Move left pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1  # Move right pointer until it finds a vowel

            if left < right:  
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1

        return "".join(s)  # Convert list back to a string
