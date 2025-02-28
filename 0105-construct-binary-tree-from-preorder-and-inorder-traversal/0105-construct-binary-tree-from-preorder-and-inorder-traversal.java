import java.util.HashMap;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    private Map<Integer, Integer> inorderMap;
    private int preorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderMap = new HashMap<>();
        preorderIndex = 0;

        // Store inorder values and their indices in a HashMap for quick lookup
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return construct(preorder, 0, inorder.length - 1);
    }

    private TreeNode construct(int[] preorder, int left, int right) {
        // Base case: If the left index exceeds the right, return null
        if (left > right) {
            return null;
        }

        // Get the current root value from preorder traversal
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);

        // Get the index of root value in inorder traversal
        int inorderIndex = inorderMap.get(rootValue);

        // Recursively build left and right subtrees
        root.left = construct(preorder, left, inorderIndex - 1);
        root.right = construct(preorder, inorderIndex + 1, right);

        return root;
    }

    // Helper function to print tree in preorder for verification
    public void printTree(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        printTree(root.left);
        printTree(root.right);
    }

    public static void main(String[] args) {
        Solution builder = new Solution();
        int[] preorder = {3, 9, 20, 15, 7};
        int[] inorder = {9, 3, 15, 20, 7};

        TreeNode root = builder.buildTree(preorder, inorder);
        builder.printTree(root); // Expected Output: 3 9 20 15 7
    }
}
