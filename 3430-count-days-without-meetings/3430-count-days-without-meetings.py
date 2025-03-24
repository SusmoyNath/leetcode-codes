from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Step 1: Sort meetings based on start day
        meetings.sort()
        
        merged = []
        for start, end in meetings:
            if merged and merged[-1][1] >= start - 1:  # Merge overlapping or contiguous meetings
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        # Step 2: Count the free days
        free_days = merged[0][0] - 1  # Days before the first meeting
        for i in range(1, len(merged)):
            free_days += merged[i][0] - merged[i - 1][1] - 1  # Gap between merged meetings
        
        free_days += days - merged[-1][1]  # Days after the last meeting
        
        return free_days
