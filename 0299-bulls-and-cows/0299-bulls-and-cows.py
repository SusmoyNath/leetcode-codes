from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_freq = Counter()
        guess_freq = Counter()
        
        # Step 1: Count Bulls and track non-matching digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_freq[s] += 1
                guess_freq[g] += 1
        
        # Step 2: Count Cows
        cows = sum(min(secret_freq[d], guess_freq[d]) for d in secret_freq)
        
        return f"{bulls}A{cows}B"
