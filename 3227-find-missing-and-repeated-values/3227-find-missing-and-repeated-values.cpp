class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        int n_squared = n * n;
        
        // Use long long to prevent overflow
        long long actual_sum = (long long)n_squared * (n_squared + 1) / 2;
        long long actual_square_sum = (long long)n_squared * (n_squared + 1) * (2 * n_squared + 1) / 6;
        
        long long observed_sum = 0, observed_square_sum = 0;
        int repeated = -1;
        unordered_map<int, int> count;
        
        for (const auto& row : grid) {
            for (int num : row) {
                observed_sum += num;
                observed_square_sum += (long long) num * num;
                count[num]++;
                if (count[num] == 2) repeated = num;
            }
        }
        
        // Let x = missing number, y = repeated number
        long long diff_sum = actual_sum - observed_sum;  // x - y
        long long diff_square_sum = actual_square_sum - observed_square_sum; // x^2 - y^2
        
        // Compute missing value using derived formula
        int missing = (diff_square_sum / diff_sum + diff_sum) / 2;
        
        return {repeated, missing};
    }
};
