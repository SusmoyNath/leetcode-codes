import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Long, Integer> memo = new HashMap<>();

    public int integerReplacement(int n) {
        return helper((long) n);
    }

    private int helper(long n) {
        if (n == 1) return 0;
        if (memo.containsKey(n)) return memo.get(n);

        int steps;
        if (n % 2 == 0) {
            steps = 1 + helper(n / 2);
        } else {
            steps = 1 + Math.min(helper(n + 1), helper(n - 1));
        }

        memo.put(n, steps);
        return steps;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.integerReplacement(8));  // Output: 3
        System.out.println(sol.integerReplacement(7));  // Output: 4
        System.out.println(sol.integerReplacement(4));  // Output: 2
    }
}
