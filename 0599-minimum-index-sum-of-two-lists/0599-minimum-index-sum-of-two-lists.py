class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {word: i for i, word in enumerate(list1)}  # Store index of words in list1
        min_sum = float('inf')
        result = []
        
        for j, word in enumerate(list2):
            if word in index_map:  # Check if word is in list1
                index_sum = j + index_map[word]  # Calculate index sum
                if index_sum < min_sum:  # Found a smaller index sum
                    min_sum = index_sum
                    result = [word]
                elif index_sum == min_sum:  # Found another word with the same minimum sum
                    result.append(word)
        
        return result
