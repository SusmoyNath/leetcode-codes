class Solution(object):
    def findWords(self, words):
        # Define the rows as sets for quick lookup
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        # Check each word
        for word in words:
            lower_word = set(word.lower())  # Convert to lowercase and set for easy checking
            
            # If the entire word's characters belong to any one row, add it to result
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(word)
        
        return result
