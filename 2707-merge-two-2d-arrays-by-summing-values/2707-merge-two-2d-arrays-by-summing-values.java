import java.util.*;

class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        List<int[]> result = new ArrayList<>();
        int i = 0, j = 0;

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i][0] == nums2[j][0]) { 
                result.add(new int[]{nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++; j++;  // Move both pointers
            } else if (nums1[i][0] < nums2[j][0]) {
                result.add(nums1[i]);
                i++;  // Move nums1 pointer
            } else {
                result.add(nums2[j]);
                j++;  // Move nums2 pointer
            }
        }

        // Add remaining elements
        while (i < nums1.length) result.add(nums1[i++]);
        while (j < nums2.length) result.add(nums2[j++]);

        return result.toArray(new int[result.size()][]);
    }

    // Test function
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] nums1 = {{1,2}, {2,3}, {4,5}};
        int[][] nums2 = {{1,4}, {3,2}, {4,1}};

        int[][] result = solution.mergeArrays(nums1, nums2);

        for (int[] pair : result) {
            System.out.println(Arrays.toString(pair));
        }
    }
}
