public class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        
        Node head = root; // Start of the current level
        while (head != null) {
            Node dummy = new Node(0); // Dummy node for the next level
            Node curr = dummy;
            
            while (head != null) { // Iterate over the current level
                if (head.left != null) {
                    curr.next = head.left;
                    curr = curr.next;
                }
                if (head.right != null) {
                    curr.next = head.right;
                    curr = curr.next;
                }
                head = head.next; // Move within the level
            }
            
            head = dummy.next; // Move to the next level
        }
        
        return root;
    }
}
