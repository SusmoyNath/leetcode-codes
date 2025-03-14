class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')  # Count total spaces
        words = text.split()  # Extract words by splitting on whitespace
        
        if len(words) == 1:
            return words[0] + ' ' * space_count  # If only one word, all spaces go at the end

        space_between = space_count // (len(words) - 1)  # Evenly distributed spaces
        extra_spaces = space_count % (len(words) - 1)  # Extra spaces to be added at the end

        return (' ' * space_between).join(words) + ' ' * extra_spaces
