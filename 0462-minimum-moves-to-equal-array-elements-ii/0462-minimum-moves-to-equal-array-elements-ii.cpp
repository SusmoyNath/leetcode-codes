#include <vector>
#include <algorithm>

class Solution {
public:
    int minMoves2(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());  // Step 1: Sort the array
        int median = nums[nums.size() / 2];   // Step 2: Find the median
        int moves = 0;
        
        // Step 3: Calculate total moves
        for (int num : nums) {
            moves += std::abs(num - median);
        }
        
        return moves;
    }
};
