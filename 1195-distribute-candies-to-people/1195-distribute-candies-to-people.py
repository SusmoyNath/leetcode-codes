from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0  # Counter to track the number of candies to give
        
        while candies > 0:
            give = min(i + 1, candies)  # Give either i+1 candies or remaining candies
            result[i % num_people] += give  # Distribute to the correct person
            candies -= give  # Deduct candies
            i += 1  # Move to next turn
        
        return result
