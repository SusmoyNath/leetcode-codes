class Solution {
    private static final int MOD = 1000000007;

    public int checkRecord(int n) {
        if (n == 1) return 3;
        if (n == 2) return 8;

        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 4;

        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
        }

        long result = dp[n];

        for (int i = 0; i < n; i++) {
            result = (result + (dp[i] * dp[n - i - 1]) % MOD) % MOD;
        }

        return (int) result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 10101;
        System.out.println(solution.checkRecord(n)); // Expected: 183236316
    }
}
