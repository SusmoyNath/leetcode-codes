#include <vector>

using namespace std;

// Solution class (Remove duplicate Node definition)
class Solution {
public:
    void helper(Node* root, vector<int>& result) {
        if (!root) return;
        
        result.push_back(root->val); // Visit root
        
        for (Node* child : root->children) {
            helper(child, result); // Visit children recursively
        }
    }

    vector<int> preorder(Node* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }
};
