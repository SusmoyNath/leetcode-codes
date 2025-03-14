class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles  # Start by drinking all initial bottles
        empty_bottles = numBottles  # Initially, all bottles become empty
        
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange  # Exchange empty bottles for new full bottles
            total_drunk += new_bottles  # Drink these new bottles
            empty_bottles = new_bottles + (empty_bottles % numExchange)  # Update remaining empty bottles
        
        return total_drunk
