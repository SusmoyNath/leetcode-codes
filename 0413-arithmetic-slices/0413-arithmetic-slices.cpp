class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) return 0;  // At least 3 elements required

        int count = 0, total_slices = 0;
        
        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                count++;
                total_slices += count;
            } else {
                count = 0; // Reset count if the sequence breaks
            }
        }
        
        return total_slices;
    }
};
