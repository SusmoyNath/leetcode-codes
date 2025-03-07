from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):  # Iterate till len(s) - 10 + 1
            sub = s[i:i + 10]  # Extract 10-letter substring
            if sub in seen:
                repeated.add(sub)  # If seen before, add to repeated set
            seen.add(sub)  # Store substring in seen set

        return list(repeated)
