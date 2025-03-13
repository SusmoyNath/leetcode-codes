#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int count = 0;
        int n = points.size();

        for (int i = 0; i < n; i++) {
            unordered_map<int, int> distCount; // Map to store distance frequency

            for (int j = 0; j < n; j++) {
                if (i == j) continue; // Skip same point
                
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int distSq = dx * dx + dy * dy; // Squared distance to avoid precision issues
                
                distCount[distSq]++; // Increment count of this distance
            }

            // Calculate the number of valid boomerangs
            for (auto& [_, freq] : distCount) {
                if (freq > 1) {
                    count += freq * (freq - 1); // Permutation count: P(n,2) = n * (n-1)
                }
            }
        }

        return count;
    }
};
