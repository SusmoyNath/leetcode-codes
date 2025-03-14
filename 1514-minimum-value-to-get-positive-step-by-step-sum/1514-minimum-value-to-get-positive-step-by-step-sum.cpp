class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int sum = 0, min_prefix_sum = 0;
        
        for (int num : nums) {
            sum += num;
            min_prefix_sum = min(min_prefix_sum, sum);
        }
        
        return 1 - min_prefix_sum;
    }
};
