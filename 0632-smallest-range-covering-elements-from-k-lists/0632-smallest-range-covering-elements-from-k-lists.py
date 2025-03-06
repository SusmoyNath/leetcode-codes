import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []  # Min heap to track the smallest element in the current window
        max_val = float('-inf')  # Track the max value in the current window
        range_start, range_end = float('-inf'), float('inf')

        # Step 1: Insert the first element of each list into the heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list index, element index)
            max_val = max(max_val, nums[i][0])  # Update max value in the window

        # Step 2: Process elements in the heap to find the smallest range
        while min_heap:
            min_val, list_idx, ele_idx = heapq.heappop(min_heap)  # Get the smallest element

            # Update the smallest range found so far
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val

            # If we reach the end of any list, stop (we can't cover all lists anymore)
            if ele_idx + 1 == len(nums[list_idx]):
                break

            # Insert the next element from the same list into the heap
            next_val = nums[list_idx][ele_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, ele_idx + 1))
            max_val = max(max_val, next_val)  # Update max value

        return [range_start, range_end]

# Example Usage
sol = Solution()
print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))  # Output: [20,24]
print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))  # Output: [1,1]
