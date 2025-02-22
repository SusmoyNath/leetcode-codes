class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root, bool isLeft = false) {
        if (!root) return 0;
        
        // If it's a left leaf, add its value
        if (isLeft && !root->left && !root->right) 
            return root->val;

        // Recur for left and right children
        return sumOfLeftLeaves(root->left, true) + sumOfLeftLeaves(root->right, false);
    }
};