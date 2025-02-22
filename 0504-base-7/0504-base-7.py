class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        res = []
        
        while num > 0:
            res.append(str(num % 7))  # Get remainder (Base 7 digit)
            num //= 7  # Reduce num by dividing it by 7
        
        if negative:
            res.append("-")  # Add negative sign for negative numbers
        
        return "".join(res[::-1])  # Reverse the result and return as a string
