class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m * n  # If no operations, return the whole matrix size
        min_ai = min(op[0] for op in ops)
        min_bi = min(op[1] for op in ops)
        return min_ai * min_bi
