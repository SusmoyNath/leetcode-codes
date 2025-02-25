#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] < nums[right]) {
                right = mid;  // Minimum is in the left half (including mid)
            } 
            else if (nums[mid] > nums[right]) {
                left = mid + 1;  // Minimum is in the right half
            } 
            else {  
                right--;  // Reduce search space when nums[mid] == nums[right]
            }
        }
        
        return nums[left];
    }
};
