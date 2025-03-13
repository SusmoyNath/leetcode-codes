class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        int sum = 0, F = 0;

        // Compute initial F(0) and sum of elements
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            F += i * nums[i];
        }

        int maxF = F;

        // Compute F(k) using the formula: F(k) = F(k-1) + sum - n * nums[n-k]
        for (int k = 1; k < n; k++) {
            F = F + sum - n * nums[n - k];
            maxF = Math.max(maxF, F);
        }

        return maxF;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxRotateFunction(new int[]{4, 3, 2, 6})); // Output: 26
        System.out.println(sol.maxRotateFunction(new int[]{100})); // Output: 0
    }
}
