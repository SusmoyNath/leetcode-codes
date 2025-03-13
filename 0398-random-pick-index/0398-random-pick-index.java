import java.util.Random;

class Solution {
    private int[] nums;
    private Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        this.rand = new Random();
    }
    
    public int pick(int target) {
        int result = -1, count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                count++;
                // Reservoir Sampling: Probability = 1/count
                if (rand.nextInt(count) == 0) {
                    result = i;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution(new int[]{1, 2, 3, 3, 3});
        System.out.println(solution.pick(3));  // Random index from {2, 3, 4}
        System.out.println(solution.pick(1));  // 0
        System.out.println(solution.pick(3));  // Random index from {2, 3, 4}
    }
}
