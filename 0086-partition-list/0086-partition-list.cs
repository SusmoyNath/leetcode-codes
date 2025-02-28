public class Solution {
    public ListNode Partition(ListNode head, int x) {
        // Create two dummy nodes to represent the heads of two partitions
        ListNode lessHead = new ListNode(0);
        ListNode greaterEqualHead = new ListNode(0);
        
        // These pointers will help in building the two partitions
        ListNode less = lessHead;
        ListNode greaterEqual = greaterEqualHead;
        
        // Traverse the original list
        while (head != null) {
            if (head.val < x) {
                less.next = head;  // Add to 'less' partition
                less = less.next;
            } else {
                greaterEqual.next = head;  // Add to 'greaterEqual' partition
                greaterEqual = greaterEqual.next;
            }
            head = head.next;
        }
        
        // Connect the two partitions
        greaterEqual.next = null;  // Ensure the last node points to null
        less.next = greaterEqualHead.next;  // Connect less partition to greaterEqual partition
        
        // Return the merged list starting from the first node of the less partition
        return lessHead.next;
    }
}
