var uniquePathsWithObstacles = function(obstacleGrid) {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;

    // If the start or end has an obstacle, return 0 as no path exists
    if (obstacleGrid[0][0] === 1 || obstacleGrid[m - 1][n - 1] === 1) {
        return 0;
    }

    // Create a dp table initialized to 0
    let dp = Array(m).fill().map(() => Array(n).fill(0));

    // Set the starting point
    dp[0][0] = 1;

    // Fill the first column (only one way to go down unless there's an obstacle)
    for (let i = 1; i < m; i++) {
        if (obstacleGrid[i][0] === 0) {
            dp[i][0] = dp[i - 1][0];
        }
    }

    // Fill the first row (only one way to go right unless there's an obstacle)
    for (let j = 1; j < n; j++) {
        if (obstacleGrid[0][j] === 0) {
            dp[0][j] = dp[0][j - 1];
        }
    }

    // Fill the rest of the dp table
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (obstacleGrid[i][j] === 0) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // Paths from above and left
            } else {
                dp[i][j] = 0; // Obstacle, no path
            }
        }
    }

    // The result is the value in the bottom-right corner
    return dp[m - 1][n - 1];
};
