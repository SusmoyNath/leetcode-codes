import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        min_radius = 0

        for house in houses:
            # Find the position where the heater should be
            pos = bisect.bisect_left(heaters, house)
            
            # Calculate distances to the closest heater(s)
            left_distance = abs(house - heaters[pos - 1]) if pos > 0 else float('inf')
            right_distance = abs(house - heaters[pos]) if pos < len(heaters) else float('inf')
            
            # Take the minimum distance to a heater
            min_radius = max(min_radius, min(left_distance, right_distance))

        return min_radius
