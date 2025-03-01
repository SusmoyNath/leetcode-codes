import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class Solution {  // Changed class name from PathSumII to Solution
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), result);
        return result;
    }
    
    private void dfs(TreeNode node, int targetSum, List<Integer> path, List<List<Integer>> result) {
        if (node == null) return;
        
        path.add(node.val);
        targetSum -= node.val;
        
        if (node.left == null && node.right == null && targetSum == 0) {
            result.add(new ArrayList<>(path));
        } else {
            dfs(node.left, targetSum, path, result);
            dfs(node.right, targetSum, path, result);
        }
        
        path.remove(path.size() - 1); // Backtracking
    }
}
