from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))  # Sort the word
            anagrams[sorted_word].append(word)  # Group by sorted version

        return list(anagrams.values())
