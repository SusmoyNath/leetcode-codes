class Solution {
    public int longestSubstring(String s, int k) {
        return helper(s, 0, s.length(), k);
    }

    private int helper(String s, int start, int end, int k) {
        if (end - start < k) return 0; // If the substring length is smaller than k, return 0
        
        // Frequency count of characters
        int[] count = new int[26];
        for (int i = start; i < end; i++) {
            count[s.charAt(i) - 'a']++;
        }

        // Identify a character that appears less than k times
        for (int i = start; i < end; i++) {
            if (count[s.charAt(i) - 'a'] < k) {
                // Split at this point
                int left = helper(s, start, i, k);
                int right = helper(s, i + 1, end, k);
                return Math.max(left, right);
            }
        }

        // If all characters appear at least k times, return the substring length
        return end - start;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestSubstring("aaabb", 3)); // Output: 3
        System.out.println(sol.longestSubstring("ababbc", 2)); // Output: 5
    }
}
