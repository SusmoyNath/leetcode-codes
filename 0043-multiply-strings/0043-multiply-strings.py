class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":  # Edge case: Multiplication with zero
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # Max possible length of the product
        
        # Reverse iterate through num1 and num2 (right to left)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]

                result[pos2] = total % 10  # Store the unit place
                result[pos1] += total // 10  # Carry to the next left position
        
        # Convert result array to string (skip leading zeros)
        result_str = "".join(map(str, result)).lstrip("0")
        
        return result_str if result_str else "0"  # Ensure we donât return empty string
