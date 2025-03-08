class Solution {
public:
    void dfs(TreeNode* node, int depth, vector<int>& result) {
        if (!node) return;
        
        // If it's the first node we're visiting at this depth, add it
        if (depth == result.size()) {
            result.push_back(node->val);
        }

        // Traverse right first, then left
        dfs(node->right, depth + 1, result);
        dfs(node->left, depth + 1, result);
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        dfs(root, 0, result);
        return result;
    }
};
