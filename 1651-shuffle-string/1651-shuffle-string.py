from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        shuffled = [""] * n  # Create an empty list of the same length as s
        for i, char in enumerate(s):
            shuffled[indices[i]] = char  # Place character at the correct index
        return "".join(shuffled)  # Join list into a string
