class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<double> dp(m + 1, 0);  // Using double to avoid integer overflow
        dp[0] = 1;  // Base case: One way to match an empty string
        
        for (int i = 1; i <= n; i++) {
            // Traverse backwards to avoid overwriting previous row values
            for (int j = m; j >= 1; j--) {
                if (s[i-1] == t[j-1]) {
                    dp[j] += dp[j-1];
                }
            }
        }
        return (int)dp[m];
    }
};
