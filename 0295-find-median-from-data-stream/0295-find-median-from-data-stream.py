import heapq

class MedianFinder:
    def __init__(self):
        # Max heap (simulated using negative values) for the left half
        self.left = []  
        # Min heap for the right half
        self.right = []  

    def addNum(self, num: int) -> None:
        # Step 1: Insert into max heap (left)
        heapq.heappush(self.left, -num)

        # Step 2: Balance - Ensure max of left <= min of right
        if self.left and self.right and (-self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: Maintain size property (left can have at most one extra element)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # If odd, return max of left
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, return average of both roots
        return (-self.left[0] + self.right[0]) / 2.0
