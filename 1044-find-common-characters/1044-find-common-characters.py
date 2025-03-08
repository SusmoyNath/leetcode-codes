from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize with the character count of the first word
        common_count = Counter(words[0])

        # Iterate over the rest of the words and update common_count
        for word in words[1:]:
            word_count = Counter(word)  # Get character count of current word
            for char in list(common_count.keys()):
                common_count[char] = min(common_count[char], word_count[char])
                if common_count[char] == 0:
                    del common_count[char]

        # Convert the final common_count dictionary into a list of characters
        result = []
        for char, freq in common_count.items():
            result.extend([char] * freq)

        return result
