#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> positions;
        
        for (int i = 0; i < n; i++) {
            positions[nums[i]].push_back(i);
        }
        
        vector<int> ans(n, -1);
        
        for (auto& [value, indices] : positions) {
            if (indices.size() < 2) continue;
            
            sort(indices.begin(), indices.end());
            int m = indices.size();
            
            for (int i = 0; i < m; i++) {
                int cur = indices[i];
                int nextIdx = (i == m - 1) ? indices[0] + n : indices[i+1];
                int nextDiff = nextIdx - cur;
                int prevIdx = (i == 0) ? indices[m-1] - n : indices[i-1];
                int prevDiff = cur - prevIdx;
                ans[cur] = min(nextDiff, prevDiff);
            }
        }
        
        vector<int> answer;
        for (int q : queries) {
            answer.push_back(ans[q]);
        }
        return answer;
    }
};
