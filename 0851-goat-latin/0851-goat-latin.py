class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        
        for i, word in enumerate(words):
            if word[0] in vowels:
                words[i] = word + "ma"
            else:
                words[i] = word[1:] + word[0] + "ma"
            
            words[i] += "a" * (i + 1)  # Append 'a' (i+1) times
        
        return " ".join(words)
