class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}  # Store first index of each character
        max_length = -1  # Initialize with -1 (if no valid substring found)

        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the length of substring between first and current occurrence
                max_length = max(max_length, i - first_occurrence[char] - 1)
            else:
                # Store first occurrence index
                first_occurrence[char] = i
        
        return max_length
