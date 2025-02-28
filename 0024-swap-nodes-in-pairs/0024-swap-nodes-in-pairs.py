class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        # Swap first and second
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second  # New head
