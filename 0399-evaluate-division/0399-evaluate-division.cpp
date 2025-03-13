#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, unordered_map<string, double>> graph;
        
        // Step 1: Build Graph
        for (int i = 0; i < equations.size(); i++) {
            string A = equations[i][0], B = equations[i][1];
            double value = values[i];
            graph[A][B] = value;          // A / B = value
            graph[B][A] = 1.0 / value;    // B / A = 1 / value
        }

        // Step 2: Process Queries
        vector<double> results;
        for (const auto& query : queries) {
            string C = query[0], D = query[1];
            
            if (graph.find(C) == graph.end() || graph.find(D) == graph.end()) {
                results.push_back(-1.0);  // If either variable is unknown
            } else if (C == D) {
                results.push_back(1.0);   // C / C = 1.0
            } else {
                unordered_set<string> visited;
                double result = dfs(graph, C, D, 1.0, visited);
                results.push_back(result);
            }
        }
        return results;
    }

private:
    // DFS function to find the result of division
    double dfs(unordered_map<string, unordered_map<string, double>>& graph, string current, string target, double product, unordered_set<string>& visited) {
        if (current == target) return product;
        
        visited.insert(current);
        
        for (const auto& neighbor : graph[current]) {
            if (visited.find(neighbor.first) == visited.end()) {
                double result = dfs(graph, neighbor.first, target, product * neighbor.second, visited);
                if (result != -1.0) return result;  // If valid path found
            }
        }
        
        return -1.0;  // No valid path
    }
};
