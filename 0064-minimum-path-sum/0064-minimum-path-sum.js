var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    
    // Create a 2D DP table
    let dp = Array(m).fill().map(() => Array(n).fill(0));

    // Initialize the starting point
    dp[0][0] = grid[0][0];

    // Fill the first row (can only come from the left)
    for (let j = 1; j < n; j++) {
        dp[0][j] = dp[0][j - 1] + grid[0][j];
    }

    // Fill the first column (can only come from above)
    for (let i = 1; i < m; i++) {
        dp[i][0] = dp[i - 1][0] + grid[i][0];
    }

    // Fill the rest of the dp table
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
        }
    }

    // The result is the value at the bottom-right corner
    return dp[m - 1][n - 1];
};
