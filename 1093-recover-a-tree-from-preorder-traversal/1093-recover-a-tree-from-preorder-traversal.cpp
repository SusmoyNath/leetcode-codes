#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    TreeNode* recoverFromPreorder(string traversal) {
        stack<pair<TreeNode*, int>> stk;  // Stack stores (node, depth)
        int i = 0, n = traversal.size();

        while (i < n) {
            int depth = 0;
            while (i < n && traversal[i] == '-') {
                depth++;
                i++;
            }

            int value = 0;
            while (i < n && isdigit(traversal[i])) {
                value = value * 10 + (traversal[i] - '0');
                i++;
            }

            TreeNode* node = new TreeNode(value);

            while (!stk.empty() && stk.top().second >= depth) {
                stk.pop();
            }

            if (!stk.empty()) {
                if (!stk.top().first->left) {
                    stk.top().first->left = node;
                } else {
                    stk.top().first->right = node;
                }
            }

            stk.push({node, depth});
        }

        // Root of the tree will be the first element added to the stack
        while (stk.size() > 1) {
            stk.pop();
        }

        return stk.top().first;
    }
};