from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Count word frequencies in both sentences
        word_count = Counter(s1.split()) + Counter(s2.split())
        
        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
