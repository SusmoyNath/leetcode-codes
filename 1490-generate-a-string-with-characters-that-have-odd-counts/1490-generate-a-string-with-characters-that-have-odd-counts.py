class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n  # All 'a' (odd count)
        else:
            return 'a' * (n - 1) + 'b'  # n-1 'a' and 1 'b' (odd count for each)
