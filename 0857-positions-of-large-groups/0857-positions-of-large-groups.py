class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        n = len(s)
        i = 0  # Start index of the group
        
        while i < n:
            j = i  # j will extend till the end of the group
            while j < n - 1 and s[j] == s[j + 1]:
                j += 1
            
            if j - i + 1 >= 3:  # Group size check
                res.append([i, j])
            
            i = j + 1  # Move to the next group
        
        return res
