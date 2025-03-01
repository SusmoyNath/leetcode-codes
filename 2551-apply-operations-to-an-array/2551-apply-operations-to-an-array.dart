class Solution {
  List<int> applyOperations(List<int> nums) {
    int n = nums.length;
    
    // Step 1: Apply the operations
    for (int i = 0; i < n - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
    }
    
    // Step 2: Move all non-zero elements forward and push zeros to the end
    List<int> result = [];
    for (int num in nums) {
      if (num != 0) {
        result.add(num);
      }
    }
    
    // Append zeros to the end
    while (result.length < n) {
      result.add(0);
    }
    
    return result;
  }
}