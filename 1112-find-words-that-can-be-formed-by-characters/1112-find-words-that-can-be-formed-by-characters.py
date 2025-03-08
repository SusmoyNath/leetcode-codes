from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Count frequency of characters in chars
        char_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            # Check if word can be formed using chars
            if all(word_count[c] <= char_count[c] for c in word):
                total_length += len(word)
        
        return total_length