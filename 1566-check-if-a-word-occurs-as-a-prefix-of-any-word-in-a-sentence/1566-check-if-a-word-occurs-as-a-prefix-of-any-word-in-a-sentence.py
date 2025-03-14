class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # Split sentence into words
        for i, word in enumerate(words):
            if word.startswith(searchWord):  # Check if it's a prefix
                return i + 1  # Return 1-based index
        return -1  # No match found
