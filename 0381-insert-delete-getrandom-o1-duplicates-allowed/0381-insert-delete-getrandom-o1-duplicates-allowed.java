import java.util.*;

class RandomizedCollection {
    private List<Integer> list;
    private Map<Integer, Set<Integer>> map;
    private Random rand;

    public RandomizedCollection() {
        list = new ArrayList<>();
        map = new HashMap<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        boolean isNew = !map.containsKey(val);
        
        // Insert val at the end of the list
        list.add(val);
        
        // Add index to map
        map.putIfAbsent(val, new HashSet<>());
        map.get(val).add(list.size() - 1);
        
        return isNew;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val) || map.get(val).isEmpty()) return false;

        // Get any index of val
        int removeIndex = map.get(val).iterator().next();
        int lastIndex = list.size() - 1;
        int lastValue = list.get(lastIndex);

        // Remove removeIndex from map
        map.get(val).remove(removeIndex);

        if (removeIndex != lastIndex) {
            // Move lastValue to removeIndex
            list.set(removeIndex, lastValue);
            // Update map: replace lastIndex with removeIndex
            map.get(lastValue).remove(lastIndex);
            map.get(lastValue).add(removeIndex);
        }
        
        // Remove last element from list
        list.remove(lastIndex);
        
        // Clean up map if no indices left
        if (map.get(val).isEmpty()) {
            map.remove(val);
        }
        
        return true;
    }
    
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }
}
