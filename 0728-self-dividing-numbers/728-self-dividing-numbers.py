from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(n: int) -> bool:
            for digit in str(n):
                if digit == '0' or n % int(digit) != 0:
                    return False
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]

# Example usage
sol = Solution()
print(sol.selfDividingNumbers(1, 22))  # Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(sol.selfDividingNumbers(47, 85))  # Output: [48,55,66,77]
