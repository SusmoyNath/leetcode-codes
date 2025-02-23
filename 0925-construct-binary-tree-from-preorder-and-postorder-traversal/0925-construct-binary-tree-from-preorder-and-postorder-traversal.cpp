#include <vector>
#include <unordered_map>
using namespace std;

// No need to redefine TreeNode (LeetCode provides it)

class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        unordered_map<int, int> postIndex;  // Store postorder indices for quick lookup
        for (int i = 0; i < postorder.size(); i++) {
            postIndex[postorder[i]] = i;
        }
        int preIndex = 0;
        return buildTree(preorder, postorder, postIndex, preIndex, 0, postorder.size() - 1);
    }

private:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& postorder, unordered_map<int, int>& postIndex, 
                        int& preIndex, int left, int right) {
        if (left > right) return nullptr;  // Base case

        TreeNode* root = new TreeNode(preorder[preIndex++]); // Create root node

        if (left == right) return root; // Leaf node, return immediately
        
        // Find left subtree root in postorder
        int leftRootIndex = postIndex[preorder[preIndex]];

        // Recursively build left and right subtrees
        root->left = buildTree(preorder, postorder, postIndex, preIndex, left, leftRootIndex);
        root->right = buildTree(preorder, postorder, postIndex, preIndex, leftRootIndex + 1, right - 1);

        return root;
    }
};
