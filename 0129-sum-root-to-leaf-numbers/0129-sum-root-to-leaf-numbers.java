class Solution {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }
    
    private int dfs(TreeNode node, int currentSum) {
        if (node == null) return 0;
        
        currentSum = currentSum * 10 + node.val;

        // If it's a leaf node, return the current number
        if (node.left == null && node.right == null) {
            return currentSum;
        }

        // Recursively calculate sum for left and right subtrees
        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
    }
}
