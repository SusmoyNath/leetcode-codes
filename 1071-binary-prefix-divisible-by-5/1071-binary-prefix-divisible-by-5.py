from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0  # To store the decimal value of the binary prefix

        for bit in nums:
            num = (num * 2 + bit) % 5  # Only keep remainder to prevent overflow
            result.append(num == 0)

        return result
