class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;

        // Step 1: Sort intervals by end time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1]; // Sort by end time
        });

        int removeCount = 0;
        int prevEnd = intervals[0][1]; // First interval's end time

        // Step 2: Iterate through intervals
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < prevEnd) { // Overlapping condition
                removeCount++; // Remove the current interval
            } else {
                prevEnd = intervals[i][1]; // Update prevEnd
            }
        }

        return removeCount;
    }
};
