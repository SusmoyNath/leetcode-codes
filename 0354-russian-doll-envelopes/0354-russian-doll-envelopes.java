import java.util.*;

class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes.length == 0) return 0;

        // Step 1: Sort by width ASC, and by height DESC when widths are equal
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] == b[0]) return b[1] - a[1]; // Sort heights in descending order
            return a[0] - b[0]; // Sort widths in ascending order
        });

        // Step 2: Find LIS on the heights using Patience Sorting (Binary Search)
        List<Integer> lis = new ArrayList<>();

        for (int[] envelope : envelopes) {
            int height = envelope[1];

            // Find the index to place height in the LIS array
            int idx = binarySearch(lis, height);
            
            // If the height is larger than all elements, add it to the LIS array
            if (idx == lis.size()) {
                lis.add(height);
            } else {
                lis.set(idx, height);
            }
        }

        return lis.size();
    }

    // Binary search helper function to find the position to replace or insert the height
    private int binarySearch(List<Integer> lis, int target) {
        int left = 0, right = lis.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (lis.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left; // Position to replace or insert
    }
}
