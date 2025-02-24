class Solution {
public:
    int maxSum = INT_MIN; // Stores the global max path sum

    int dfs(TreeNode* root) {
        if (!root) return 0; // Base case: Null node contributes 0

        // Recursively find the max sum of left and right subtrees
        int left = max(0, dfs(root->left));   // Ignore negative paths
        int right = max(0, dfs(root->right)); // Ignore negative paths

        // Update the global max path sum considering the full path through root
        maxSum = max(maxSum, left + right + root->val);

        // Return max single branch sum (either left or right, plus root)
        return max(left, right) + root->val;
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return maxSum;
    }
};
