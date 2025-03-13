#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;  // Convert value to index (1-based to 0-based)
            
            if (nums[index] < 0) {
                result.push_back(abs(nums[i]));  // If already negative, it's a duplicate
            } else {
                nums[index] = -nums[index];  // Mark as visited
            }
        }

        return result;
    }
};
