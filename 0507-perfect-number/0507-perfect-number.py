class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False  # No perfect numbers â¤ 1
        
        divisor_sum = 1  # Start with 1 (since every number is divisible by 1)
        sqrt_num = int(num ** 0.5)
        
        for i in range(2, sqrt_num + 1):
            if num % i == 0:  # Found a divisor
                divisor_sum += i
                if i != num // i:  # Add the paired divisor
                    divisor_sum += num // i
        
        return divisor_sum == num  # Check if sum equals num
