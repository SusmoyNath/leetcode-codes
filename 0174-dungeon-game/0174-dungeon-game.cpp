#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        
        vector<vector<int>> health(m, vector<int>(n, 0));
        
        // Base Case: Bottom-right cell (princess' cell)
        health[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]);
        
        // Fill last row (only move right)
        for (int j = n - 2; j >= 0; j--) {
            health[m-1][j] = max(1, health[m-1][j+1] - dungeon[m-1][j]);
        }
        
        // Fill last column (only move down)
        for (int i = m - 2; i >= 0; i--) {
            health[i][n-1] = max(1, health[i+1][n-1] - dungeon[i][n-1]);
        }
        
        // Fill the rest of the table
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                int min_health = min(health[i+1][j], health[i][j+1]);
                health[i][j] = max(1, min_health - dungeon[i][j]);
            }
        }
        
        return health[0][0];
    }
};
