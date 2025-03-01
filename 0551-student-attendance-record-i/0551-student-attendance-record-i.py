class Solution:
    def checkRecord(self, s: str) -> bool:
        # Condition 1: Count absences
        if s.count('A') >= 2:
            return False
        
        # Condition 2: Check for three consecutive 'L'
        if "LLL" in s:
            return False
        
        return True
