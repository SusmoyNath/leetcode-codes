class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] prefixSum = new long[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        return mergeSort(prefixSum, 0, prefixSum.length - 1, lower, upper);
    }

    private int mergeSort(long[] sum, int left, int right, int lower, int upper) {
        if (left >= right) return 0;
        
        int mid = left + (right - left) / 2;
        int count = mergeSort(sum, left, mid, lower, upper) + mergeSort(sum, mid + 1, right, lower, upper);
        
        int j = mid + 1, k = mid + 1, t = mid + 1;
        long[] temp = new long[right - left + 1];
        int idx = 0;
        
        for (int i = left; i <= mid; i++) {
            while (k <= right && sum[k] - sum[i] < lower) k++;
            while (j <= right && sum[j] - sum[i] <= upper) j++;
            count += j - k;

            // Merge the two sorted halves
            while (t <= right && sum[t] < sum[i]) temp[idx++] = sum[t++];
            temp[idx++] = sum[i];
        }
        
        // Copy the merged values back to the original array
        System.arraycopy(temp, 0, sum, left, idx);
        
        return count;
    }
}
