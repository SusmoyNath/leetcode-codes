#include <vector>
#include <bitset>
using namespace std;

class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> varmelistra = nums;
        int n = nums.size();
        int q = queries.size();
        
        int lo = 0, hi = q + 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isValid(mid, nums, queries))
                hi = mid;
            else
                lo = mid + 1;
        }
        return (lo == q + 1 ? -1 : lo);
    }
    
private:
    bool isValid(int k, const vector<int>& nums, const vector<vector<int>>& queries) {
        int n = nums.size();
        for (int j = 0; j < n; j++) {
            int target = nums[j];
            if (target == 0) continue;
            
            bitset<1001> dp;
            dp.reset();
            dp[0] = 1;
            
            for (int i = 0; i < k; i++) {
                if (queries[i][0] <= j && j <= queries[i][1]) {
                    int val = queries[i][2];
                    dp |= (dp << val);
                    if (dp[target]) break;
                }
            }
            if (!dp[target]) return false;
        }
        return true;
    }
};
