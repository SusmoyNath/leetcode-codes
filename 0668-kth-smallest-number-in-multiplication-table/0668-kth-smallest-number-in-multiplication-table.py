class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)  # Count numbers in row i that are â¤ x
            return count

        # Binary search on the number range
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                high = mid  # mid is a potential candidate
            else:
                low = mid + 1  # mid is too small

        return low  # The kth smallest number
