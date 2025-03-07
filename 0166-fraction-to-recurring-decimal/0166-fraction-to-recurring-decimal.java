import java.util.*;

class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0"; // If numerator is 0, result is 0.

        StringBuilder result = new StringBuilder();

        // Handle negative cases
        if ((numerator < 0) ^ (denominator < 0)) result.append("-");

        // Convert to long to prevent overflow
        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);

        // Append the integer part
        result.append(num / den);
        long remainder = num % den;

        // If there is no fractional part, return the result
        if (remainder == 0) return result.toString();

        result.append(".");

        // Map to store remainder positions
        Map<Long, Integer> map = new HashMap<>();

        while (remainder != 0) {
            if (map.containsKey(remainder)) {
                result.insert(map.get(remainder), "(");
                result.append(")");
                break;
            }

            // Store the remainder's position
            map.put(remainder, result.length());

            remainder *= 10;
            result.append(remainder / den);
            remainder %= den;
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fractionToDecimal(1, 2));    // Output: "0.5"
        System.out.println(sol.fractionToDecimal(2, 1));    // Output: "2"
        System.out.println(sol.fractionToDecimal(4, 333));  // Output: "0.(012)"
        System.out.println(sol.fractionToDecimal(-50, 8));  // Output: "-6.25"
    }
}
