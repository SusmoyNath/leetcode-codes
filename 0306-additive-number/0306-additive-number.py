class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Helper function to check if a sequence is valid
        def is_valid(num1: int, num2: int, start: int) -> bool:
            while start < n:
                num3 = num1 + num2
                num3_str = str(num3)
                
                if not num.startswith(num3_str, start):
                    return False
                
                start += len(num3_str)
                num1, num2 = num2, num3  # Move to the next pair
            
            return True  # If we successfully reach the end, it's valid

        # Try every possible split for the first two numbers
        for i in range(1, n):  # First number: num[:i]
            for j in range(i + 1, n):  # Second number: num[i:j]
                num1, num2 = num[:i], num[i:j]

                # Leading zero check: numbers must not start with '0' unless they are "0"
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                if is_valid(int(num1), int(num2), j):  
                    return True  # Found a valid sequence

        return False  # No valid sequence found
