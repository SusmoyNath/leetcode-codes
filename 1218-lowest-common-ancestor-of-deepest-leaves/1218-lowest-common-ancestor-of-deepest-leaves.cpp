class Solution {
public:
    // Helper function returns a pair: (LCA node, depth)
    pair<TreeNode*, int> dfs(TreeNode* node) {
        if (!node) return {nullptr, 0};
        
        auto [leftNode, leftDepth] = dfs(node->left);
        auto [rightNode, rightDepth] = dfs(node->right);
        
        if (leftDepth > rightDepth) {
            return {leftNode, leftDepth + 1};
        } else if (rightDepth > leftDepth) {
            return {rightNode, rightDepth + 1};
        } else {
            return {node, leftDepth + 1}; // same depth â this node is the LCA
        }
    }
    
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root).first;
    }
};
