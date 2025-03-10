from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [word for word in words if any(word in other for other in words if word != other)]