class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1  # At least one character exists
        current_power = 1  # Current streak length
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:  # If current char matches previous
                current_power += 1
                max_power = max(max_power, current_power)  # Update max power
            else:
                current_power = 1  # Reset streak
        
        return max_power
