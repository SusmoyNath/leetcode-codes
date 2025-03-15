class Solution {
public:
    bool canRob(vector<int>& nums, int k, int capability) {
        int count = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            if (nums[i] <= capability) { // If we can rob this house
                count++; 
                i++; // Skip the next house to maintain non-adjacency
            }
            if (count >= k) return true; // Already selected k houses
        }
        
        return false;
    }

    int minCapability(vector<int>& nums, int k) {
        int low = *min_element(nums.begin(), nums.end());
        int high = *max_element(nums.begin(), nums.end());

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (canRob(nums, k, mid)) {
                high = mid; // Try for a smaller capability
            } else {
                low = mid + 1; // Increase capability if k houses cannot be robbed
            }
        }
        
        return low;
    }
};
