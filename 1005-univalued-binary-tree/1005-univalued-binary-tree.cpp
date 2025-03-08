class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        if (!root) return true; // Base case: Empty tree is considered uni-valued.
        return dfs(root, root->val);
    }

private:
    bool dfs(TreeNode* node, int val) {
        if (!node) return true; // Reached the end of a branch, still uni-valued.
        if (node->val != val) return false; // If value mismatch, return false.
        return dfs(node->left, val) && dfs(node->right, val); // Check left and right subtrees.
    }
};
