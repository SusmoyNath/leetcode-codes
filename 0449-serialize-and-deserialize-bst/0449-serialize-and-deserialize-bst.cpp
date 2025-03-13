#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

class Codec {
public:
    // Encodes a tree to a single string (Preorder Traversal)
    string serialize(TreeNode* root) {
        stringstream ss;
        serializeHelper(root, ss);
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<int> preorder;
        stringstream ss(data);
        string token;
        
        // Convert the string back to preorder values
        while (getline(ss, token, ' ')) {
            if (!token.empty()) preorder.push_back(stoi(token));
        }
        
        int index = 0;
        return deserializeHelper(preorder, index, INT_MIN, INT_MAX);
    }

private:
    // Helper function for serialization
    void serializeHelper(TreeNode* root, stringstream& ss) {
        if (!root) return;
        ss << root->val << " ";  // Store current node value
        serializeHelper(root->left, ss);
        serializeHelper(root->right, ss);
    }

    // Helper function for deserialization
    TreeNode* deserializeHelper(vector<int>& preorder, int& index, int minVal, int maxVal) {
        if (index >= preorder.size()) return nullptr;
        
        int val = preorder[index];
        if (val < minVal || val > maxVal) return nullptr;

        TreeNode* root = new TreeNode(val);
        index++;
        root->left = deserializeHelper(preorder, index, minVal, val);
        root->right = deserializeHelper(preorder, index, val, maxVal);
        return root;
    }
};

// Usage Example:
// Codec ser, deser;
// string tree = ser.serialize(root);
// TreeNode* ans = deser.deserialize(tree);
