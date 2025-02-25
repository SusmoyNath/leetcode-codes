#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        if (n <= 2) return n; // If 1 or 2 points, they are trivially on the same line
        
        int maxCount = 1;
        
        for (int i = 0; i < n; i++) {
            unordered_map<string, int> slopeCount;
            int samePoint = 0, vertical = 0, localMax = 0;
            
            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0 && dy == 0) {
                    samePoint++;  // Identical points
                    continue;
                }
                if (dx == 0) {
                    vertical++; // Vertical line case
                    localMax = max(localMax, vertical);
                    continue;
                }

                // Reduce fraction to simplest form
                int g = __gcd(dx, dy);
                dx /= g;
                dy /= g;

                // Store as a string "dy/dx" to avoid floating point precision issues
                string slope = to_string(dy) + "/" + to_string(dx);
                slopeCount[slope]++;

                localMax = max(localMax, slopeCount[slope]);
            }
            
            maxCount = max(maxCount, localMax + samePoint + 1);
        }
        
        return maxCount;
    }
};
