class Solution {
    public int countBinarySubstrings(String s) {
        int prevGroup = 0, currGroup = 1, count = 0;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                currGroup++;  // Extend the current group
            } else {
                count += Math.min(prevGroup, currGroup); // Count valid substrings
                prevGroup = currGroup; // Update previous group size
                currGroup = 1; // Reset current group size
            }
        }

        return count + Math.min(prevGroup, currGroup); // Add the last counted group
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countBinarySubstrings("00110011")); // Output: 6
        System.out.println(sol.countBinarySubstrings("10101"));    // Output: 4
    }
}
