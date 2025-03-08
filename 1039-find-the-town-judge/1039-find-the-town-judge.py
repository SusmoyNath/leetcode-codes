from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1  # If there's only one person and no trust relationships, they are the judge.

        trust_counts = [0] * (n + 1)  # Trust count array

        for a, b in trust:
            trust_counts[a] -= 1  # Outgoing trust (disqualifies from being judge)
            trust_counts[b] += 1  # Incoming trust (potential judge)

        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:  # The judge should be trusted by everyone else
                return i

        return -1  # No judge found
