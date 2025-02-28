public class Solution {
    public int NumDecodings(string s) {
        // If the string is empty or starts with '0', there's no valid decoding.
        if (string.IsNullOrEmpty(s) || s[0] == '0') {
            return 0;
        }
        
        int n = s.Length;
        int[] dp = new int[n + 1];
        dp[0] = 1; // Base case: there's one way to decode an empty string.
        dp[1] = 1; // Base case: there's one way to decode a non-empty string if it's not '0'.
        
        for (int i = 2; i <= n; i++) {
            // Single digit decoding (s[i-1])
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // Two digit decoding (s[i-2] and s[i-1])
            int twoDigit = int.Parse(s.Substring(i - 2, 2));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        
        return dp[n];
    }
}
