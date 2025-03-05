#include <vector>

using namespace std;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0, right = letters.size();
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (letters[mid] > target)
                right = mid;  // Search left half
            else
                left = mid + 1;  // Search right half
        }
        
        // If no greater letter is found, return the first letter (circular wrap)
        return letters[left % letters.size()];
    }
};
