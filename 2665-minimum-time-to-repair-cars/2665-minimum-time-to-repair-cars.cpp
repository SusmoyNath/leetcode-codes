class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long left = 1, right = 1LL * (*min_element(ranks.begin(), ranks.end())) * cars * cars;
        long long ans = right;

        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long repaired = 0;
            
            for (int r : ranks) {
                repaired += (long long) sqrt(mid / r); // Number of cars this mechanic can repair
                if (repaired >= cars) break; // Stop early if we've already repaired enough
            }

            if (repaired >= cars) {
                ans = mid;
                right = mid - 1; // Try for a smaller time
            } else {
                left = mid + 1; // Increase time
            }
        }

        return ans;
    }
};
