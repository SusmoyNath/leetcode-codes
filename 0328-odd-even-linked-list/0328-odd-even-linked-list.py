from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # No need to process if 0 or 1 node
        
        odd = head  # Points to first odd node
        even = head.next  # Points to first even node
        even_head = even  # Store start of even list
        
        while even and even.next:
            odd.next = even.next  # Skip one node (point to next odd)
            odd = odd.next  # Move odd forward
            
            even.next = odd.next  # Skip one node (point to next even)
            even = even.next  # Move even forward
        
        # Connect odd list with even list
        odd.next = even_head
        
        return head
