function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head || left === right) return head;
    
    let dummy = new ListNode(0); // Create a dummy node to handle edge cases like reversing from the head.
    dummy.next = head;
    
    let prev = dummy;
    
    // Step 1: Move `prev` to the node before `left`-th position
    for (let i = 0; i < left - 1; i++) {
        prev = prev.next!;
    }
    
    // `start` will be the `left`-th node and `end` will be the `right`-th node.
    let start = prev.next!;
    let end = start.next!;
    
    // Step 2: Reverse the sublist between `left` and `right`
    for (let i = 0; i < right - left; i++) {
        start.next = end.next;
        end.next = prev.next;
        prev.next = end;
        end = start.next!;
    }
    
    return dummy.next;
}
