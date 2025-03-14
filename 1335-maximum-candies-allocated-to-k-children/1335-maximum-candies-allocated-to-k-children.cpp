class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        long long left = 1, right = *max_element(candies.begin(), candies.end());
        long long ans = 0;

        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long count = 0;

            for (int candy : candies) {
                count += candy / mid;
            }

            if (count >= k) {
                ans = mid;  // Valid split, try for more
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return ans;
    }
};
