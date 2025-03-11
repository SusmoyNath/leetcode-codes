class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total_count = 10  # f(1) = 10
        unique_digits = 9  # For n = 2, first digit has 9 choices
        available_digits = 9  # Remaining choices
        
        for i in range(2, n + 1):
            unique_digits *= available_digits  # Multiply decreasing choices
            available_digits -= 1  # Reduce choices as we use digits
            total_count += unique_digits  # Sum up all unique cases
            
        return total_count
