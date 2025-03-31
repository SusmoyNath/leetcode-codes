#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        int n = weights.size();
        if (k == 1) return 0;  // Only one bag, so max-min = 0
        
        vector<long long> splitCosts;
        for (int i = 0; i < n - 1; i++) {
            splitCosts.push_back(weights[i] + weights[i + 1]);
        }
        
        // Sort the split costs
        sort(splitCosts.begin(), splitCosts.end());
        
        // Compute the difference
        long long minScore = 0, maxScore = 0;
        for (int i = 0; i < k - 1; i++) {
            minScore += splitCosts[i];  // Smallest k-1
            maxScore += splitCosts[n - 2 - i];  // Largest k-1
        }
        
        return maxScore - minScore;
    }
};
