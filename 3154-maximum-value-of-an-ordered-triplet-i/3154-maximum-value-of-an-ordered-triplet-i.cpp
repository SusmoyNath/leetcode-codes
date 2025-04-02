class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        long long max_value = 0;

        // Store the max prefix values for i < j
        vector<int> max_prefix(n, 0);
        max_prefix[0] = nums[0];

        for (int i = 1; i < n; i++) {
            max_prefix[i] = max(max_prefix[i - 1], nums[i]);
        }

        // Iterate over j as the middle element
        for (int j = 1; j < n - 1; j++) {
            long long max_i = max_prefix[j - 1]; // Best nums[i] before j
            
            if (max_i > nums[j]) {
                // Find the best nums[k] after j
                long long max_k = 0;
                for (int k = j + 1; k < n; k++) {
                    max_k = max(max_k, (long long) nums[k]);
                }
                
                // Calculate and update max_value
                max_value = max(max_value, (max_i - nums[j]) * max_k);
            }
        }

        return max_value;
    }
};
