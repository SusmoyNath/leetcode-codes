#include <vector>

using namespace std;

class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size(), n = grid[0].size();

        // Base case: Out of bounds or water ('0')
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == '0') return;

        // Mark the cell as visited
        grid[i][j] = '0';

        // Explore all four directions (up, down, left, right)
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int count = 0;
        int m = grid.size(), n = grid[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j); // Sink the island
                }
            }
        }
        
        return count;
    }
};
