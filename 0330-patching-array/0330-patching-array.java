class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;  // Smallest missing number
        int patches = 0, i = 0;

        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i];  // Extend the range
                i++;
            } else {
                miss += miss;  // Patch the array with `miss`
                patches++;
            }
        }
        
        return patches;
    }
}
