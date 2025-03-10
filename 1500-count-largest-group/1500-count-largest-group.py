from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)  # Dictionary to store group sizes
        
        # Step 1: Compute sum of digits for each number and group them
        for num in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(num))
            groups[digit_sum] += 1  # Count the number of elements in each group

        # Step 2: Find the maximum group size
        max_size = max(groups.values())

        # Step 3: Count how many groups have this maximum size
        return sum(1 for size in groups.values() if size == max_size)