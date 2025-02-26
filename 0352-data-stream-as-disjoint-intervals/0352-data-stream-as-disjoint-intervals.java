import java.util.*;

class SummaryRanges {
    private TreeMap<Integer, Integer> intervals;

    public SummaryRanges() {
        intervals = new TreeMap<>();
    }

    public void addNum(int value) {
        if (intervals.containsKey(value)) return; // Ignore duplicate values

        Integer left = intervals.floorKey(value);
        Integer right = intervals.higherKey(value);

        boolean mergeLeft = (left != null && intervals.get(left) + 1 >= value);
        boolean mergeRight = (right != null && right - 1 <= value);

        if (mergeLeft && mergeRight) {
            // Merge both left and right intervals into one
            int newStart = left;
            int newEnd = intervals.get(right);
            intervals.remove(left);
            intervals.remove(right);
            intervals.put(newStart, newEnd);
        } else if (mergeLeft) {
            // Merge with left interval
            intervals.put(left, Math.max(intervals.get(left), value));
        } else if (mergeRight) {
            // Merge with right interval
            int end = intervals.get(right);
            intervals.remove(right);
            intervals.put(value, end);
        } else {
            // No merging, create a new interval
            intervals.put(value, value);
        }

        // Ensure merging of overlapping intervals after addition
        cleanUp();
    }

    private void cleanUp() {
        Integer prevStart = null;
        Integer prevEnd = null;
        List<Integer> toRemove = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : intervals.entrySet()) {
            int start = entry.getKey();
            int end = entry.getValue();

            if (prevEnd != null && prevEnd + 1 >= start) {
                // Merge consecutive intervals
                intervals.put(prevStart, Math.max(prevEnd, end));
                toRemove.add(start);
            } else {
                prevStart = start;
                prevEnd = end;
            }
        }

        for (int key : toRemove) {
            intervals.remove(key);
        }
    }

    public int[][] getIntervals() {
        int[][] result = new int[intervals.size()][2];
        int i = 0;
        for (Map.Entry<Integer, Integer> entry : intervals.entrySet()) {
            result[i++] = new int[]{entry.getKey(), entry.getValue()};
        }
        return result;
    }
}
