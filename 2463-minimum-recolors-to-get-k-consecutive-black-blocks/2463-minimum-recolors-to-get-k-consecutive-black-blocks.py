class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = float('inf')
        w_count = blocks[:k].count('W')  # Count 'W' in the first k-window
        min_ops = w_count  # Initialize min_ops

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':  # Remove leftmost block of previous window
                w_count -= 1
            if blocks[i] == 'W':  # Add rightmost block of new window
                w_count += 1
            min_ops = min(min_ops, w_count)  # Update min_ops

        return min_ops

# Example Usage
solution = Solution()
print(solution.minimumRecolors("WBBWWBBWBW", 7))  # Output: 3
print(solution.minimumRecolors("WBWBBBW", 2))    # Output: 0
