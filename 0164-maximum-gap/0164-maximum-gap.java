import java.util.*;

class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;

        int minNum = Integer.MAX_VALUE, maxNum = Integer.MIN_VALUE;
        for (int num : nums) {
            minNum = Math.min(minNum, num);
            maxNum = Math.max(maxNum, num);
        }
        if (minNum == maxNum) return 0;

        int n = nums.length;
        int gap = Math.max(1, (maxNum - minNum) / (n - 1));

        int bucketCount = (maxNum - minNum) / gap + 1;
        int[] bucketMin = new int[bucketCount];
        int[] bucketMax = new int[bucketCount];
        boolean[] hasBucket = new boolean[bucketCount];

        Arrays.fill(bucketMin, Integer.MAX_VALUE);
        Arrays.fill(bucketMax, Integer.MIN_VALUE);

        for (int num : nums) {
            if (num == minNum || num == maxNum) continue;
            int idx = (num - minNum) / gap;
            bucketMin[idx] = Math.min(bucketMin[idx], num);
            bucketMax[idx] = Math.max(bucketMax[idx], num);
            hasBucket[idx] = true;
        }

        int maxGap = 0, prevMax = minNum;
        for (int i = 0; i < bucketCount; i++) {
            if (!hasBucket[i]) continue;
            maxGap = Math.max(maxGap, bucketMin[i] - prevMax);
            prevMax = bucketMax[i];
        }

        return Math.max(maxGap, maxNum - prevMax);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maximumGap(new int[]{3,6,9,1})); // Output: 3
        System.out.println(sol.maximumGap(new int[]{10}));      // Output: 0
        System.out.println(sol.maximumGap(new int[]{1,10000000})); // Output: 9999999
    }
}
