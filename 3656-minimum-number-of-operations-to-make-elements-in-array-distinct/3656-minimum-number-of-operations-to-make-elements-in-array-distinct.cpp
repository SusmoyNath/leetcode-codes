class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int operations = 0;

        while (true) {
            unordered_set<int> seen(nums.begin(), nums.end());
            
            // If all elements are distinct, break
            if (seen.size() == nums.size()) {
                break;
            }

            // Otherwise, remove the first 3 elements or all if less than 3
            if (nums.size() <= 3) {
                nums.clear();
            } else {
                nums.erase(nums.begin(), nums.begin() + 3);
            }
            operations++;
        }

        return operations;
    }
};
