class Solution {
    private int[][] directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    private int m, n;
    
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        
        m = matrix.length;
        n = matrix[0].length;
        int[][] memo = new int[m][n];  // Memoization table
        int maxPath = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxPath = Math.max(maxPath, dfs(matrix, i, j, memo));
            }
        }
        
        return maxPath;
    }
    
    private int dfs(int[][] matrix, int row, int col, int[][] memo) {
        if (memo[row][col] != 0) return memo[row][col];  // Return cached result
        
        int maxLength = 1;  // Minimum path length is 1 (starting point)
        
        for (int[] dir : directions) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            
            if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && matrix[newRow][newCol] > matrix[row][col]) {
                maxLength = Math.max(maxLength, 1 + dfs(matrix, newRow, newCol, memo));
            }
        }
        
        memo[row][col] = maxLength;  // Store result in memo
        return maxLength;
    }
}
