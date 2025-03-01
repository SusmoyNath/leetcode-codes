#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        if (trees.size() <= 1) return trees;

        // Step 1: Sort by x, then by y
        sort(trees.begin(), trees.end());

        vector<vector<int>> hull;

        // Function to compute cross product (orientation)
        auto cross = [](vector<int>& p, vector<int>& q, vector<int>& r) {
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]);
        };

        // Step 2: Build the lower hull
        for (auto& t : trees) {
            while (hull.size() >= 2 && cross(hull[hull.size() - 2], hull.back(), t) < 0) {
                hull.pop_back();
            }
            hull.push_back(t);
        }

        // Step 3: Build the upper hull
        int lowerSize = hull.size();
        for (int i = trees.size() - 1; i >= 0; i--) {
            while (hull.size() > lowerSize && cross(hull[hull.size() - 2], hull.back(), trees[i]) < 0) {
                hull.pop_back();
            }
            hull.push_back(trees[i]);
        }

        // Step 4: Remove duplicate points using set
        set<vector<int>> uniqueHull(hull.begin(), hull.end());
        return vector<vector<int>>(uniqueHull.begin(), uniqueHull.end());
    }
};
