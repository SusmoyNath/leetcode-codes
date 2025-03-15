class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        vector<int> nums(n + 1, 0);
        nums[1] = 1;
        int maxVal = 1; // Track maximum value in nums

        for (int i = 1; 2 * i + 1 <= n; i++) {
            nums[2 * i] = nums[i];
            nums[2 * i + 1] = nums[i] + nums[i + 1];
            maxVal = max(maxVal, max(nums[2 * i], nums[2 * i + 1]));
        }
        
        return maxVal;
    }
};
