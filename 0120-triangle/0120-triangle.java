import java.util.List;

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        
        // Start from the second-last row and move upwards
        for (int row = n - 2; row >= 0; row--) {
            for (int col = 0; col < triangle.get(row).size(); col++) {
                // Choose the minimum path sum from below
                int minPath = Math.min(triangle.get(row + 1).get(col), triangle.get(row + 1).get(col + 1));
                triangle.get(row).set(col, triangle.get(row).get(col) + minPath);
            }
        }
        
        // The top element now contains the minimum path sum
        return triangle.get(0).get(0);
    }
}
