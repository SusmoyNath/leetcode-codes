from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])  # Length of each word
        word_count = len(words)  # Number of words
        total_len = word_len * word_count  # Total substring length
        word_freq = Counter(words)  # Frequency of words in `words`
        
        result = []

        # Try every possible alignment in `word_len` characters
        for i in range(word_len):
            left = i  # Left pointer of the sliding window
            right = i  # Right pointer
            seen_words = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len  # Move right pointer
                
                if word in word_freq:
                    seen_words[word] += 1
                    
                    # If a word appears too many times, adjust window
                    while seen_words[word] > word_freq[word]:
                        leftmost_word = s[left:left + word_len]
                        seen_words[leftmost_word] -= 1
                        left += word_len  # Shrink window

                    # If we have a valid substring
                    if right - left == total_len:
                        result.append(left)

                else:
                    # Reset window
                    seen_words.clear()
                    left = right

        return result
