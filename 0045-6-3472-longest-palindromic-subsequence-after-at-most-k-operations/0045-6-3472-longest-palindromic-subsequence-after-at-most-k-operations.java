import java.util.Arrays;

class Solution {
    public int longestPalindromicSubsequence(String s, int k) {
        int n = s.length();
        int[][][] dp = new int[n][n][k + 1];

        // Base case: Single character palindromes
        for (int i = 0; i < n; i++) {
            for (int c = 0; c <= k; c++) {
                dp[i][i][c] = 1;
            }
        }

        // Fill DP table
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                for (int mod = 0; mod <= k; mod++) {
                    // Case 1: Ignore either left or right character
                    dp[i][j][mod] = Math.max(dp[i + 1][j][mod], dp[i][j - 1][mod]);

                    // Case 2: Match characters, considering modification cost
                    int cost = getCyclicDistance(s.charAt(i), s.charAt(j));
                    if (mod >= cost) {
                        dp[i][j][mod] = Math.max(dp[i][j][mod], 2 + dp[i + 1][j - 1][mod - cost]);
                    }
                }
            }
        }

        return dp[0][n - 1][k];
    }

    // Compute minimum cyclic distance
    private int getCyclicDistance(char a, char b) {
        int dist = Math.abs(a - b);
        return Math.min(dist, 26 - dist);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestPalindromicSubsequence("abced", 2));  // Expected: 3
        System.out.println(sol.longestPalindromicSubsequence("aaazzz", 4)); // Expected: 6
    }
}
