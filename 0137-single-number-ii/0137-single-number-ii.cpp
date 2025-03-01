#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;

        for (int num : nums) {
            ones = (ones ^ num) & ~twos; // Update ones (1st occurrence)
            twos = (twos ^ num) & ~ones; // Update twos (2nd occurrence)
        }

        return ones; // 'ones' will hold the single number
    }
};
