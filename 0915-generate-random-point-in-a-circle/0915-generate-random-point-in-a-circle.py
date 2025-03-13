import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        theta = random.uniform(0, 2 * math.pi)  # Random angle between 0 and 2Ï
        r = math.sqrt(random.uniform(0, 1)) * self.radius  # Random radius with sqrt scaling
        
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]

# Example Usage:
# obj = Solution(1.0, 0.0, 0.0)
# print(obj.randPoint())  # Example output: [-0.02493, -0.38077]
