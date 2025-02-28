from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged is empty OR no overlap, add new interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals: merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
