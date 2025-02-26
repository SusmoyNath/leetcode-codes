import java.util.*;

class Solution {
    public boolean canCross(int[] stones) {
        int n = stones.length;
        if (stones[1] != 1) return false; // The first jump must be exactly 1
        
        // Map: stone position -> possible jump sizes
        Map<Integer, Set<Integer>> dp = new HashMap<>();
        
        for (int stone : stones) {
            dp.put(stone, new HashSet<>());
        }
        
        dp.get(0).add(1); // Frog must start with a jump of 1
        
        for (int stone : stones) {
            for (int jump : dp.get(stone)) {
                int reach = stone + jump;
                if (reach == stones[n - 1]) return true; // If we reach the last stone, return true
                
                if (dp.containsKey(reach)) {
                    if (jump - 1 > 0) dp.get(reach).add(jump - 1);
                    dp.get(reach).add(jump);
                    dp.get(reach).add(jump + 1);
                }
            }
        }
        
        return false;
    }
}
