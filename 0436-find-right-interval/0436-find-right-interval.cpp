class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> result(n, -1);
        vector<pair<int, int>> sortedIntervals;

        // Store (start, index) pairs
        for (int i = 0; i < n; i++) {
            sortedIntervals.push_back({intervals[i][0], i});
        }

        // Sort by start time
        sort(sortedIntervals.begin(), sortedIntervals.end());

        // Perform binary search for each interval's end
        for (int i = 0; i < n; i++) {
            int endValue = intervals[i][1];

            // Binary search for the smallest start >= endValue
            int left = 0, right = n - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (sortedIntervals[mid].first >= endValue) {
                    right = mid - 1;  // Look for smaller start value
                } else {
                    left = mid + 1;
                }
            }

            // If found, store the corresponding index
            if (left < n) {
                result[i] = sortedIntervals[left].second;
            }
        }

        return result;
    }
};
