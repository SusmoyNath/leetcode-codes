import java.util.*;

class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        Set<String> pointSet = new HashSet<>();
        int minX = Integer.MAX_VALUE, minY = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE, maxY = Integer.MIN_VALUE;
        int totalArea = 0;

        for (int[] rect : rectangles) {
            int x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3];
            totalArea += (x2 - x1) * (y2 - y1);

            minX = Math.min(minX, x1);
            minY = Math.min(minY, y1);
            maxX = Math.max(maxX, x2);
            maxY = Math.max(maxY, y2);

            // Store four corner points
            String[] points = {
                x1 + "," + y1, x1 + "," + y2, x2 + "," + y1, x2 + "," + y2
            };
            
            for (String p : points) {
                if (!pointSet.add(p)) {
                    pointSet.remove(p);
                }
            }
        }

        // Check total area
        int expectedArea = (maxX - minX) * (maxY - minY);
        if (totalArea != expectedArea) return false;

        // The set should contain exactly 4 corner points of the bounding rectangle
        Set<String> expectedCorners = new HashSet<>();
        expectedCorners.add(minX + "," + minY);
        expectedCorners.add(minX + "," + maxY);
        expectedCorners.add(maxX + "," + minY);
        expectedCorners.add(maxX + "," + maxY);

        return pointSet.equals(expectedCorners);
    }
}
