#include <unordered_map>
#include <vector>

using namespace std;

// Provided Node structure (DO NOT redefine)
class Solution {
public:
    unordered_map<Node*, Node*> visited;  // HashMap to store cloned nodes

    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        return dfs(node);
    }

private:
    Node* dfs(Node* node) {
        if (visited.find(node) != visited.end()) {
            return visited[node];  // Return cloned node if already visited
        }

        Node* clone = new Node(node->val);  // Create a new cloned node
        visited[node] = clone;  // Store mapping

        // Clone neighbors recursively
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor));
        }

        return clone;
    }
};
