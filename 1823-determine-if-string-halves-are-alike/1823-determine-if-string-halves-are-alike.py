class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s) // 2  # Since s.length is even, n is the midpoint
        return sum(1 for c in s[:n] if c in vowels) == sum(1 for c in s[n:] if c in vowels)
