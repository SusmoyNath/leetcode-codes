from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = second = dummy  

        # Move 'first' ahead by 'n + 1' steps
        for _ in range(n + 1):
            first = first.next  

        # Move both pointers until 'first' reaches the end
        while first:
            first, second = first.next, second.next  

        # Remove the nth node
        second.next = second.next.next  

        return dummy.next  # Return updated head
