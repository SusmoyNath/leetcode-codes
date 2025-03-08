class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (!root) return 0; // Base case: if the node is null, return 0
        
        int sum = 0;
        
        // If root value is within the range, add it to sum
        if (root->val >= low && root->val <= high) {
            sum += root->val;
        }
        
        // If root value is greater than low, search in the left subtree
        if (root->val > low) {
            sum += rangeSumBST(root->left, low, high);
        }
        
        // If root value is smaller than high, search in the right subtree
        if (root->val < high) {
            sum += rangeSumBST(root->right, low, high);
        }
        
        return sum;
    }
};
