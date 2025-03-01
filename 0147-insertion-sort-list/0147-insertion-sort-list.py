class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # Already sorted if only one or zero nodes

        dummy = ListNode(0)  # Dummy node to simplify insertion
        curr = head  # Pointer for traversing the original list

        while curr:
            prev = dummy  # Start from the dummy node each time
            next_node = curr.next  # Store the next node before re-linking

            # Find the correct position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next  # Move to the next node in sorted part

            # Insert current node in the sorted list
            curr.next = prev.next
            prev.next = curr

            # Move to the next node in the original list
            curr = next_node

        return dummy.next  # Return the sorted list's head
