class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode slow = head, fast = head;

        // Step 1: Detect if a cycle exists
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) { // Cycle detected
                slow = head;

                // Step 2: Find the cycle start node
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow; // Cycle entry point
            }
        }
        return null; // No cycle
    }
}
