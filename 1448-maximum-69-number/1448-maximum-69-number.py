class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)  # Convert number to string
        return int(num_str.replace('6', '9', 1))  # Replace the first '6' with '9' and convert back to integer
