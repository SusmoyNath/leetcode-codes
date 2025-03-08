class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>()); // Sort in descending order
        
        for (int i = 0; i < nums.size() - 2; i++) {
            if (nums[i] < nums[i + 1] + nums[i + 2]) { // Triangle condition
                return nums[i] + nums[i + 1] + nums[i + 2]; // Return the perimeter
            }
        }
        return 0; // No valid triangle found
    }
};
