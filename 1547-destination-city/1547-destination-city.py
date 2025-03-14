from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = {start for start, end in paths}  # Collect all starting cities
        for _, destination in paths:
            if destination not in starting_cities:  # Destination city has no outgoing path
                return destination
