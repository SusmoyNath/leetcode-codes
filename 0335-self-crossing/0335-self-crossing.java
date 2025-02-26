class Solution {
    public boolean isSelfCrossing(int[] distance) {
        int n = distance.length;
        if (n < 4) return false;

        for (int i = 3; i < n; i++) {
            // Case 1: Current step crosses the one 3 steps before
            if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
                return true;
            }
            
            // Case 2: Special crossing with a loop-back
            if (i >= 4 && distance[i - 1] == distance[i - 3] && distance[i] + distance[i - 4] >= distance[i - 2]) {
                return true;
            }
            
            // Case 3: Large expansion followed by inward contraction causing a crossing
            if (i >= 5 && distance[i - 2] >= distance[i - 4] && distance[i] + distance[i - 4] >= distance[i - 2] &&
                distance[i - 1] <= distance[i - 3] && distance[i - 1] + distance[i - 5] >= distance[i - 3]) {
                return true;
            }
        }
        
        return false;
    }
}
