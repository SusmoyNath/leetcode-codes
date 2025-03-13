class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int third = INT_MIN;  // This represents nums[k] (the "2" in the 132 pattern)
        stack<int> st;        // Monotonic decreasing stack to track possible nums[j] values
        
        for (int i = nums.size() - 1; i >= 0; i--) {
            // If we find a valid "1" (nums[i] < third), return true
            if (nums[i] < third) return true;

            // Maintain a decreasing stack and find the largest "2" (nums[k])
            while (!st.empty() && st.top() < nums[i]) {
                third = st.top(); // Update "third" with the popped element
                st.pop();
            }

            // Push nums[i] as a potential "3" (nums[j])
            st.push(nums[i]);
        }
        
        return false;
    }
};
