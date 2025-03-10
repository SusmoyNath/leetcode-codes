class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1  # First ugly number is 1
        
        p2 = p3 = p5 = 0  # Pointers for 2, 3, 5
        next2, next3, next5 = 2, 3, 5  # Next multiples
        
        for i in range(1, n):
            ugly[i] = min(next2, next3, next5)  # Get the next ugly number
            
            # Move the pointer(s) forward
            if ugly[i] == next2:
                p2 += 1
                next2 = ugly[p2] * 2
            if ugly[i] == next3:
                p3 += 1
                next3 = ugly[p3] * 3
            if ugly[i] == next5:
                p5 += 1
                next5 = ugly[p5] * 5
        
        return ugly[-1]  # The nth ugly number
