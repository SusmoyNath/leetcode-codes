from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(num: int) -> bool:
            return '0' in str(num)  # Check if the number contains '0'
        
        for a in range(1, n):  # Try all possible values of a from 1 to n-1
            b = n - a  # Compute b
            if not has_zero(a) and not has_zero(b):  # Ensure both a and b have no zeros
                return [a, b]

        return []  # This should never be reached as a valid pair always exists
