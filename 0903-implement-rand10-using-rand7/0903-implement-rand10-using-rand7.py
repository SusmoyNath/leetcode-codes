# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        while True:
            # Generate a random number in the range [1, 49]
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:  # Only accept numbers within 1-40
                return (num - 1) % 10 + 1  # Map it to 1-10
