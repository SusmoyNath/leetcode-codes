import java.util.*;

class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int maxSum = Integer.MIN_VALUE;

        // Iterate over all pairs of row indices
        for (int top = 0; top < m; top++) {
            int[] rowSums = new int[n]; // Array to store sum of elements between rows `top` and `bottom`

            for (int bottom = top; bottom < m; bottom++) {
                // Compute prefix sum for each column
                for (int col = 0; col < n; col++) {
                    rowSums[col] += matrix[bottom][col];
                }

                // Find max subarray sum â¤ k using Kadane + Binary Search
                maxSum = Math.max(maxSum, maxSubarraySum(rowSums, k));
                if (maxSum == k) return k; // Best possible answer
            }
        }

        return maxSum;
    }

    // Function to find the max subarray sum â¤ k using TreeSet (Binary Search)
    private int maxSubarraySum(int[] nums, int k) {
        TreeSet<Integer> prefixSums = new TreeSet<>();
        prefixSums.add(0);
        int sum = 0, maxSum = Integer.MIN_VALUE;

        for (int num : nums) {
            sum += num;
            
            // Find the smallest prefix sum â¥ (sum - k) using TreeSet.ceiling()
            Integer target = prefixSums.ceiling(sum - k);
            if (target != null) {
                maxSum = Math.max(maxSum, sum - target);
            }

            prefixSums.add(sum); // Store current prefix sum
        }

        return maxSum;
    }
}
