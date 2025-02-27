#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        vector<unordered_map<long, int>> dp(n); // Store {diff -> count} for each index
        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diff = (long)nums[i] - nums[j];

                int count = dp[j][diff]; // Get existing sequences count with diff
                dp[i][diff] += count + 1; // Extend sequences and add new pair

                result += count; // Only count sequences of length >= 3
            }
        }

        return result;
    }
};
