class Solution {
public:
    struct NodeInfo {
        int depth;
        TreeNode* parent;
    };

    void dfs(TreeNode* node, TreeNode* parent, int depth, int x, int y, NodeInfo &xInfo, NodeInfo &yInfo) {
        if (!node) return;
        
        if (node->val == x) xInfo = {depth, parent};
        if (node->val == y) yInfo = {depth, parent};

        dfs(node->left, node, depth + 1, x, y, xInfo, yInfo);
        dfs(node->right, node, depth + 1, x, y, xInfo, yInfo);
    }

    bool isCousins(TreeNode* root, int x, int y) {
        NodeInfo xInfo = {-1, nullptr}, yInfo = {-1, nullptr};
        dfs(root, nullptr, 0, x, y, xInfo, yInfo);
        return (xInfo.depth == yInfo.depth) && (xInfo.parent != yInfo.parent);
    }
};
