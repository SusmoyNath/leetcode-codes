class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        total_duration = 0
        
        for i in range(1, len(timeSeries)):
            total_duration += min(duration, timeSeries[i] - timeSeries[i - 1])
        
        return total_duration + duration  # Add full duration for the last attack
