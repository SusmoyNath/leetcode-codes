class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) return false; // If root is null, subRoot cannot be a subtree
        
        if (isSameTree(root, subRoot)) return true; // If trees match, return true

        // Recursively check left and right subtrees
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;  // Both trees are empty
        if (!s || !t || s->val != t->val) return false;  // One is null, or values don't match

        // Check both left and right subtrees
        return isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }
};
