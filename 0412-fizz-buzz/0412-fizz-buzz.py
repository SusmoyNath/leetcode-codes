class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            result.append(output if output else str(i))
        return result