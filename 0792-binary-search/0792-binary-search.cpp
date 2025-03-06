#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2; // Avoid integer overflow
            
            if (nums[mid] == target) {
                return mid; // Found target, return index
            } 
            else if (nums[mid] < target) {
                left = mid + 1; // Search right half
            } 
            else {
                right = mid - 1; // Search left half
            }
        }
        
        return -1; // Target not found
    }
};
