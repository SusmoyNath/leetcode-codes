from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start  # Ensure start < destination
        
        clockwise_distance = sum(distance[start:destination])  # Direct sum
        total_distance = sum(distance)  # Total circular route
        counterclockwise_distance = total_distance - clockwise_distance  # The other way around
        
        return min(clockwise_distance, counterclockwise_distance)  # Return shortest
