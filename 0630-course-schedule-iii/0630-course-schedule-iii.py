import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # Sort courses based on their lastDay
        courses.sort(key=lambda x: x[1])
        
        total_time = 0
        max_heap = []  # Max heap (using negative values because Python has a min heap)

        for duration, last_day in courses:
            if total_time + duration <= last_day:
                # Take the course
                heapq.heappush(max_heap, -duration)
                total_time += duration
            elif max_heap and -max_heap[0] > duration:
                # Replace the longest duration course taken so far (greedy choice)
                total_time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)

        return len(max_heap)

# Example Usage
sol = Solution()
print(sol.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))  # Output: 3
print(sol.scheduleCourse([[1,2]]))  # Output: 1
print(sol.scheduleCourse([[3,2],[4,3]]))  # Output: 0
