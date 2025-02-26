import java.util.*;

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>();
        
        // Build graph: each airport maps to a min-heap of destination airports
        for (List<String> ticket : tickets) {
            graph.computeIfAbsent(ticket.get(0), k -> new PriorityQueue<>()).add(ticket.get(1));
        }
        
        List<String> itinerary = new LinkedList<>();
        dfs("JFK", graph, itinerary);
        
        // The itinerary is built in reverse order, so reverse it
        Collections.reverse(itinerary);
        return itinerary;
    }
    
    private void dfs(String airport, Map<String, PriorityQueue<String>> graph, List<String> itinerary) {
        PriorityQueue<String> destinations = graph.get(airport);
        
        while (destinations != null && !destinations.isEmpty()) {
            String next = destinations.poll(); // Get the smallest lexicographical destination
            dfs(next, graph, itinerary);
        }
        
        // Add airport after visiting all its neighbors
        itinerary.add(airport);
    }
}
