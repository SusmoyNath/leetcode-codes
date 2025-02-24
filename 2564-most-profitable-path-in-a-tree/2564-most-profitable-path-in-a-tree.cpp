#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> tree(n);
        
        // Convert edge list to adjacency list
        for (auto& edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }

        vector<int> bobTime(n, INT_MAX);  // Bob's arrival time at each node
        unordered_map<int, int> parent;   // Store parent for backtracking Bob's path
        parent[0] = -1;

        // Step 1: Find Bob's path to node 0 using DFS
        findBobPath(tree, bob, 0, -1, 0, bobTime, parent);

        // Step 2: Find the most profitable path for Alice using DFS
        return findMaxProfit(tree, 0, -1, 0, 0, bobTime, amount);
    }

private:
    // DFS to find Bob's time to reach each node
    bool findBobPath(vector<vector<int>>& tree, int node, int target, int par, int time, 
                     vector<int>& bobTime, unordered_map<int, int>& parent) {
        if (node == target) {  
            bobTime[node] = time;
            return true;
        }

        for (int neighbor : tree[node]) {
            if (neighbor == par) continue;  // Avoid revisiting parent
            parent[neighbor] = node;  // Track parent for backtracking

            if (findBobPath(tree, neighbor, target, node, time + 1, bobTime, parent)) {
                bobTime[node] = time;  // Update Bob's time
                return true;
            }
        }
        return false;
    }

    // DFS to calculate Alice's maximum net income
    int findMaxProfit(vector<vector<int>>& tree, int node, int parent, int time, 
                      int currentProfit, vector<int>& bobTime, vector<int>& amount) {
        // Alice and Bob meet
        if (time < bobTime[node]) {
            currentProfit += amount[node];  // Alice takes full amount
        } else if (time == bobTime[node]) {
            currentProfit += amount[node] / 2;  // Alice and Bob share the amount
        }

        // If it's a leaf node, return the current profit
        bool isLeaf = true;
        int maxProfit = INT_MIN;
        for (int neighbor : tree[node]) {
            if (neighbor == parent) continue;  // Avoid revisiting parent
            isLeaf = false;
            maxProfit = max(maxProfit, findMaxProfit(tree, neighbor, node, time + 1, 
                                                     currentProfit, bobTime, amount));
        }

        return isLeaf ? currentProfit : maxProfit;
    }
};
