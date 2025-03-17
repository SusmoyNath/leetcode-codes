class Solution:
    def reformatNumber(self, number: str) -> str:
        # Step 1: Remove spaces and dashes efficiently
        digits = [ch for ch in number if ch.isdigit()]

        # Step 2: Process the digits and format them
        n = len(digits)
        result = []
        i = 0

        while n > 4:
            result.append("".join(digits[i:i+3]))  # Take first 3 digits
            i += 3
            n -= 3

        # Step 3: Handle the last 2-4 digits
        if n == 4:
            result.append("".join(digits[i:i+2]))
            result.append("".join(digits[i+2:i+4]))
        else:
            result.append("".join(digits[i:]))

        return "-".join(result)
