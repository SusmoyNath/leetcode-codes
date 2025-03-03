import java.util.*;

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>(); // Frequency map
        Map<Integer, Integer> firstIndex = new HashMap<>(); // First occurrence map
        int degree = 0, minLength = Integer.MAX_VALUE;
        
        // First pass: Compute frequency, first occurrence, and degree
        for (int i = 0; i < nums.length; i++) {
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
            firstIndex.putIfAbsent(nums[i], i); // Store first index
            degree = Math.max(degree, count.get(nums[i])); // Update max degree
        }
        
        // Second pass: Find the smallest subarray with the same degree
        Map<Integer, Integer> lastIndex = new HashMap<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            lastIndex.putIfAbsent(nums[i], i);
        }
        
        for (int num : count.keySet()) {
            if (count.get(num) == degree) {
                minLength = Math.min(minLength, lastIndex.get(num) - firstIndex.get(num) + 1);
            }
        }
        
        return minLength;
    }
}
