class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int evenIndex = 0, oddIndex = 1;
        int n = nums.length;

        while (evenIndex < n && oddIndex < n) {
            if (nums[evenIndex] % 2 == 0) {
                evenIndex += 2;  // Correctly placed even number, move forward
            } else if (nums[oddIndex] % 2 == 1) {
                oddIndex += 2;   // Correctly placed odd number, move forward
            } else {
                // Swap misplaced even and odd numbers
                int temp = nums[evenIndex];
                nums[evenIndex] = nums[oddIndex];
                nums[oddIndex] = temp;

                evenIndex += 2;
                oddIndex += 2;
            }
        }

        return nums;
    }
}
