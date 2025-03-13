#include <unordered_map>

class Solution {
public:
    int count = 0;
    
    void dfs(TreeNode* node, long long currentSum, int targetSum, unordered_map<long long, int>& prefixSumMap) {
        if (!node) return;
        
        // Update current path sum
        currentSum += node->val;
        
        // Check if there exists a prefix sum that makes up targetSum
        if (prefixSumMap.find(currentSum - targetSum) != prefixSumMap.end()) {
            count += prefixSumMap[currentSum - targetSum];
        }
        
        // Add currentSum to prefix map
        prefixSumMap[currentSum]++;
        
        // Recur for left and right children
        dfs(node->left, currentSum, targetSum, prefixSumMap);
        dfs(node->right, currentSum, targetSum, prefixSumMap);
        
        // Backtrack: Remove the current sum from map before going back
        prefixSumMap[currentSum]--;
    }
    
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> prefixSumMap;
        prefixSumMap[0] = 1;  // To count paths that start at the root
        
        dfs(root, 0, targetSum, prefixSumMap);
        
        return count;
    }
};
