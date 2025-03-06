import java.util.*;

class Solution {
    public int minStickers(String[] stickers, String target) {
        int n = target.length();
        int[] dp = new int[1 << n]; // Bitmask DP (1 << n) states
        Arrays.fill(dp, -1);
        dp[0] = 0; // Base case: empty target needs 0 stickers
        
        int res = dfs(stickers, target, (1 << n) - 1, dp);
        return res == Integer.MAX_VALUE ? -1 : res;
    }

    private int dfs(String[] stickers, String target, int mask, int[] dp) {
        if (mask == 0) return 0;  // If target is empty, return 0 stickers
        if (dp[mask] != -1) return dp[mask];

        dp[mask] = Integer.MAX_VALUE;
        for (String sticker : stickers) {
            int newMask = mask;
            int[] count = new int[26];
            
            // Count letter frequencies in the sticker
            for (char c : sticker.toCharArray()) count[c - 'a']++;

            // Try applying this sticker
            for (int i = 0; i < target.length(); i++) {
                char c = target.charAt(i);
                if (((mask >> i) & 1) == 1 && count[c - 'a'] > 0) { // If char needed
                    count[c - 'a']--; // Use one letter
                    newMask ^= (1 << i); // Remove from target
                }
            }
            
            if (newMask != mask) { // If progress was made
                int subRes = dfs(stickers, target, newMask, dp);
                if (subRes != Integer.MAX_VALUE) {
                    dp[mask] = Math.min(dp[mask], subRes + 1);
                }
            }
        }
        return dp[mask];
    }
}

// â Test Cases
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        String[] stickers1 = {"with","example","science"};
        String target1 = "thehat";
        System.out.println(sol.minStickers(stickers1, target1)); // Expected: 3

        String[] stickers2 = {"notice","possible"};
        String target2 = "basicbasic";
        System.out.println(sol.minStickers(stickers2, target2)); // Expected: -1
    }
}
