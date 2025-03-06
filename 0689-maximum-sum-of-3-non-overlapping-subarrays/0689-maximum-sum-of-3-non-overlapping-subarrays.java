import java.util.*;

class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] sum = new int[n + 1];  // Prefix sum
        for (int i = 0; i < n; i++) {
            sum[i + 1] = sum[i] + nums[i];
        }

        int[] left = new int[n];  // Best left subarray start index
        int[] right = new int[n]; // Best right subarray start index
        int maxLeft = sum[k] - sum[0], maxRight = sum[n] - sum[n - k];
        left[k - 1] = 0;
        right[n - k] = n - k;

        // Compute left max subarray
        for (int i = k; i < n; i++) {
            int currentSum = sum[i + 1] - sum[i + 1 - k];
            if (currentSum > maxLeft) {
                maxLeft = currentSum;
                left[i] = i + 1 - k;
            } else {
                left[i] = left[i - 1];
            }
        }

        // Compute right max subarray (right to left)
        for (int i = n - k - 1; i >= 0; i--) {
            int currentSum = sum[i + k] - sum[i];
            if (currentSum >= maxRight) {  // Greedy ensures lexicographically smallest
                maxRight = currentSum;
                right[i] = i;
            } else {
                right[i] = right[i + 1];
            }
        }

        // Find best middle subarray
        int maxSum = 0;
        int[] result = new int[3];
        for (int i = k; i <= n - 2 * k; i++) {
            int l = left[i - 1], r = right[i + k];
            int total = (sum[l + k] - sum[l]) + (sum[i + k] - sum[i]) + (sum[r + k] - sum[r]);
            if (total > maxSum) {
                maxSum = total;
                result[0] = l;
                result[1] = i;
                result[2] = r;
            }
        }

        return result;
    }
}

// â Test Cases
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums1 = {1,2,1,2,6,7,5,1};
        int k1 = 2;
        System.out.println(Arrays.toString(sol.maxSumOfThreeSubarrays(nums1, k1))); // Expected: [0, 3, 5]

        int[] nums2 = {1,2,1,2,1,2,1,2,1};
        int k2 = 2;
        System.out.println(Arrays.toString(sol.maxSumOfThreeSubarrays(nums2, k2))); // Expected: [0, 2, 4]
    }
}
