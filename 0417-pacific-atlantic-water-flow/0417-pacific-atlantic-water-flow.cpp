class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> result;
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // Lambda function for DFS traversal
        function<void(int, int, vector<vector<bool>>&)> dfs = [&](int r, int c, vector<vector<bool>>& ocean) {
            ocean[r][c] = true;
            vector<int> directions = {-1, 0, 1, 0, -1}; // Up, Right, Down, Left
            
            for (int i = 0; i < 4; i++) {
                int nr = r + directions[i];
                int nc = c + directions[i + 1];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && 
                    !ocean[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    dfs(nr, nc, ocean);
                }
            }
        };

        // Start DFS from Pacific (Top row and Left column)
        for (int i = 0; i < m; i++) dfs(i, 0, pacific); // Left column
        for (int j = 0; j < n; j++) dfs(0, j, pacific); // Top row

        // Start DFS from Atlantic (Bottom row and Right column)
        for (int i = 0; i < m; i++) dfs(i, n - 1, atlantic); // Right column
        for (int j = 0; j < n; j++) dfs(m - 1, j, atlantic); // Bottom row

        // Collect cells that can reach both oceans
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
};
