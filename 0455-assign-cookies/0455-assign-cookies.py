class Solution(object):
    def findContentChildren(self, g, s):
        # Step 1: Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        # Step 2: Use two pointers to match cookies to children
        child_i, cookie_i = 0, 0
        while child_i < len(g) and cookie_i < len(s):
            if s[cookie_i] >= g[child_i]:  # If cookie satisfies the child
                child_i += 1  # Move to the next child
            cookie_i += 1  # Move to the next cookie
        
        return child_i  # Number of satisfied children