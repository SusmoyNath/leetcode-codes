class Solution:
    def partition(self, s: str):
        res = []
        self.backtrack(s, 0, [], res)
        return res

    def backtrack(self, s, start, path, res):
        if start == len(s):  # Base case: reached the end of the string
            res.append(path[:])
            return
        
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                path.append(s[start:end+1])  # Choose
                self.backtrack(s, end + 1, path, res)  # Explore
                path.pop()  # Unchoose (backtrack)

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
