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
    private int postorderIndex;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderMap = new HashMap<>();
        postorderIndex = postorder.length - 1; // Start from the last element in postorder

        // Store inorder values and their indices in a HashMap for quick lookup
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return construct(postorder, 0, inorder.length - 1);
    }

    private TreeNode construct(int[] postorder, int left, int right) {
        // Base case: If the left index exceeds the right, return null
        if (left > right) {
            return null;
        }

        // Get the current root value from postorder traversal
        int rootValue = postorder[postorderIndex--];
        TreeNode root = new TreeNode(rootValue);

        // Get the index of root value in inorder traversal
        int inorderIndex = inorderMap.get(rootValue);

        // Recursively build right and left subtrees
        root.right = construct(postorder, inorderIndex + 1, right);
        root.left = construct(postorder, left, inorderIndex - 1);

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
        int[] inorder = {9, 3, 15, 20, 7};
        int[] postorder = {9, 15, 7, 20, 3};

        TreeNode root = builder.buildTree(inorder, postorder);
        builder.printTree(root); // Expected Output: 3 9 20 15 7
    }
}
