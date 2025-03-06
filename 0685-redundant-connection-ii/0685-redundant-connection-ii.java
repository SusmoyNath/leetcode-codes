import java.util.*;

class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1];
        int[] candidate1 = null, candidate2 = null;
        
        // Step 1: Find the node with two parents
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            if (parent[v] != 0) {  // v already has a parent
                candidate1 = new int[]{parent[v], v};
                candidate2 = new int[]{u, v};
                edge[1] = 0;  // Temporarily remove this edge
            }
            parent[v] = u;
        }

        // Step 2: Union-Find to detect cycles
        int[] root = new int[n + 1];
        for (int i = 1; i <= n; i++) root[i] = i;
        
        for (int[] edge : edges) {
            if (edge[1] == 0) continue;  // Skip temporarily removed edge
            int u = edge[0], v = edge[1];
            int rootU = find(root, u), rootV = find(root, v);
            if (rootU == rootV) {  // Cycle detected
                return candidate1 == null ? edge : candidate1;
            }
            root[rootV] = rootU;
        }

        return candidate2; // If no cycle, return the second conflicting edge
    }

    private int find(int[] root, int x) {
        if (root[x] != x) {
            root[x] = find(root, root[x]);  // Path compression
        }
        return root[x];
    }
}

// â Test Cases
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] edges1 = {{1,2},{1,3},{2,3}};
        int[][] edges2 = {{1,2},{2,3},{3,4},{4,1},{1,5}};

        System.out.println(Arrays.toString(sol.findRedundantDirectedConnection(edges1))); // Expected: [2,3]
        System.out.println(Arrays.toString(sol.findRedundantDirectedConnection(edges2))); // Expected: [4,1]
    }
}
