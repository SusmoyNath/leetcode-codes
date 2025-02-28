var minDistance = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;
    
    // Create a 2D DP array
    const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));
    
    // Initialize the base cases
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;  // Deleting all characters from word1
    }
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;  // Inserting all characters into word1
    }
    
    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (word1[i - 1] === word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];  // No operation needed if characters match
            } else {
                dp[i][j] = Math.min(
                    dp[i - 1][j] + 1,  // Deletion
                    dp[i][j - 1] + 1,  // Insertion
                    dp[i - 1][j - 1] + 1  // Replacement
                );
            }
        }
    }
    
    // The result is the minimum operations to convert word1 to word2
    return dp[m][n];
};
