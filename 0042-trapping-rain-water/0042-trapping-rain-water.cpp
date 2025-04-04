#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;

        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0, water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax)
                    leftMax = height[left];  // Update leftMax
                else
                    water += leftMax - height[left];  // Water trapped at left

                left++;
            } else {
                if (height[right] >= rightMax)
                    rightMax = height[right];  // Update rightMax
                else
                    water += rightMax - height[right];  // Water trapped at right

                right--;
            }
        }

        return water;
    }
};
