class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return 0;

        // Step 1: Compute prefix maximum
        vector<int> prefix_max(n, 0);
        prefix_max[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefix_max[i] = max(prefix_max[i - 1], nums[i]);
        }

        // Step 2: Compute suffix maximum
        vector<int> suffix_max(n, 0);
        suffix_max[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffix_max[i] = max(suffix_max[i + 1], nums[i]);
        }

        // Step 3: Iterate through possible j values and compute max triplet value
        long long max_value = 0;
        for (int j = 1; j < n - 1; j++) {
            long long left_max = prefix_max[j - 1];
            long long right_max = suffix_max[j + 1];
            long long triplet_value = (left_max - nums[j]) * right_max;
            max_value = max(max_value, triplet_value);
        }

        return max_value;
    }
};
