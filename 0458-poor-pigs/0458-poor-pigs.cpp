#include <cmath>

class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int T = minutesToTest / minutesToDie; // Number of test rounds possible
        int pigs = 0;
        
        while (pow(T + 1, pigs) < buckets) {
            pigs++; // Increment pigs until we can cover all buckets
        }
        
        return pigs;
    }
};
