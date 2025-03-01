#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) return 0;

        stack<pair<Node*, int>> stk;
        stk.push({root, 1});
        int max_depth = 0;

        while (!stk.empty()) {
            auto [node, depth] = stk.top();
            stk.pop();
            max_depth = max(max_depth, depth);
            for (auto child : node->children) {
                if (child) stk.push({child, depth + 1});
            }
        }

        return max_depth;
    }
};
