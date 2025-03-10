class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2  # Divide by 2 if even
            else:
                num -= 1  # Subtract 1 if odd
            steps += 1
        return steps