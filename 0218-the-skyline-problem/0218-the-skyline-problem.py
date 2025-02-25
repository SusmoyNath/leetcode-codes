import heapq

class Solution:
    def getSkyline(self, buildings):
        # Step 1: Create events for building start and end
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start of a building
            events.append((right, 0, None))  # End of a building
        
        # Step 2: Sort the events
        events.sort()

        # Step 3: Process events using a max heap
        result = []
        max_heap = [(0, float('inf'))]  # Max heap storing (-height, end)
        prev_max = 0  # Track the previous max height
        
        for x, neg_height, right in events:
            if neg_height < 0:  # Start of a building
                heapq.heappush(max_heap, (neg_height, right))
            else:  # End of a building
                # Remove all buildings that ended
                while max_heap and max_heap[0][1] <= x:
                    heapq.heappop(max_heap)
            
            # Step 4: Check if max height has changed
            curr_max = -max_heap[0][0]  # Get current max height
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max
        
        return result
