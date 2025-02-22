import math

class Solution(object):
    def constructRectangle(self, area):
        # Start with the square root of area (largest possible square width)
        W = int(math.sqrt(area))

        # Find the largest W that evenly divides the area
        while area % W != 0:
            W -= 1
        
        L = area // W  # Compute corresponding length
        return [L, W]
