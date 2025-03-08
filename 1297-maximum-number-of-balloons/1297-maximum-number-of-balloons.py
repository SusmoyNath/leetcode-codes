from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)  # Count character occurrences
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])