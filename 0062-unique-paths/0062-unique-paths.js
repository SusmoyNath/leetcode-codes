var uniquePaths = function(m, n) {
    // Create a 2D array for storing the number of unique paths at each cell
    let dp = Array(m).fill().map(() => Array(n).fill(1));
    
    // Fill the dp table based on the recurrence relation
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1]; // Sum paths from top and left
        }
    }
    
    // Return the value at the bottom-right corner
    return dp[m-1][n-1];
};
