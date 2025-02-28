public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        // Create a dummy node to handle edge cases easily (like removing the first node)
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        while (head != null) {
            // Check if current node is a duplicate
            if (head.next != null && head.val == head.next.val) {
                // Skip all duplicate nodes
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                // Connect the previous node to the next non-duplicate node
                prev.next = head.next;
            } else {
                // If it's not a duplicate, move the prev pointer forward
                prev = prev.next;
            }
            // Move to the next node
            head = head.next;
        }
        
        // Return the list starting from the node after the dummy node
        return dummy.next;
    }
}
