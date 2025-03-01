import java.util.*;

class Solution {
    public String nearestPalindromic(String n) {
        long num = Long.parseLong(n);
        int len = n.length();
        
        // Special case: if n is 1, the closest palindrome is 0
        if (num == 1) return "0";
        
        // Generate candidate palindromes
        HashSet<Long> candidates = new HashSet<>();
        
        // Edge case candidates
        candidates.add((long) Math.pow(10, len) + 1);  // 100..001 (one more digit)
        candidates.add((long) Math.pow(10, len - 1) - 1); // 99..99 (one less digit)
        
        // Generate palindrome by mirroring the first half
        long firstHalf = Long.parseLong(n.substring(0, (len + 1) / 2));
        
        for (long i = firstHalf - 1; i <= firstHalf + 1; i++) {
            String prefix = String.valueOf(i);
            String palindrome;
            if (len % 2 == 0) {
                palindrome = prefix + new StringBuilder(prefix).reverse().toString();
            } else {
                palindrome = prefix + new StringBuilder(prefix.substring(0, prefix.length() - 1)).reverse().toString();
            }
            candidates.add(Long.parseLong(palindrome));
        }

        // Find the closest palindrome
        long closest = -1;
        long minDiff = Long.MAX_VALUE;
        
        for (long candidate : candidates) {
            if (candidate == num) continue;
            long diff = Math.abs(candidate - num);
            if (diff < minDiff || (diff == minDiff && candidate < closest)) {
                closest = candidate;
                minDiff = diff;
            }
        }

        return String.valueOf(closest);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.nearestPalindromic("123")); // Output: "121"
        System.out.println(solution.nearestPalindromic("1"));   // Output: "0"
    }
}
