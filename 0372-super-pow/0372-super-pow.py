from typing import List

class Solution:
    MODULO = 1337

    def mod_exp(self, a: int, b: int) -> int:
        """Computes (a^b) % 1337 using fast exponentiation."""
        res = 1
        a %= self.MODULO
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % self.MODULO
            a = (a * a) % self.MODULO
            b //= 2
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        """Computes a^b % 1337 where b is represented as a list of digits."""
        if not b:
            return 1  # Base case: anything to power 0 is 1
        
        last_digit = b.pop()
        part1 = self.mod_exp(a, last_digit)  # a^(last_digit) % 1337
        part2 = self.mod_exp(self.superPow(a, b), 10)  # (a^remaining_b) ^ 10 % 1337
        
        return (part1 * part2) % self.MODULO
