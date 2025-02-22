class Solution(object):
    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1  # Pointers at the last digit
        carry = 0  # Carry for addition
        result = []  # Stores the final sum
        
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0  # Convert char to int
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0  # Convert char to int
            
            total = digit1 + digit2 + carry  # Sum of digits + carry
            result.append(str(total % 10))  # Store last digit of sum
            carry = total // 10  # Update carry
            
            i -= 1  # Move left in num1
            j -= 1  # Move left in num2
        
        return ''.join(result[::-1])  # Reverse result and return as string