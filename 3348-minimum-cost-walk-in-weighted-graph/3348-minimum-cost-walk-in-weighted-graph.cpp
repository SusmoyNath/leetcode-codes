class Solution {
public:
    class DSU {
    public:
        vector<int> parent, rank, minAndValue;
        
        DSU(int n) {
            parent.resize(n);
            rank.resize(n, 1);
            minAndValue.resize(n, INT_MAX);
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        
        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]); // Path compression
            return parent[x];
        }
        
        void unite(int x, int y, int weight) {
            int rootX = find(x);
            int rootY = find(y);
            
            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                    minAndValue[rootX] &= minAndValue[rootY] & weight;
                } else if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                    minAndValue[rootY] &= minAndValue[rootX] & weight;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                    minAndValue[rootX] &= minAndValue[rootY] & weight;
                }
            } else {
                minAndValue[rootX] &= weight;
            }
        }
    };

    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DSU dsu(n);
        
        // Step 1: Construct DSU and track minimum AND cost
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            dsu.unite(u, v, w);
        }
        
        vector<int> result;
        
        // Step 2: Answer queries
        for (auto& q : query) {
            int s = q[0], t = q[1];
            if (dsu.find(s) != dsu.find(t)) {
                result.push_back(-1);
            } else {
                result.push_back(dsu.minAndValue[dsu.find(s)]);
            }
        }
        
        return result;
    }
};
