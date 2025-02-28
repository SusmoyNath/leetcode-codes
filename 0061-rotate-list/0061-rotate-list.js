var rotateRight = function(head, k) {
    if (!head || !head.next || k === 0) return head;
    
    // Find the length of the linked list
    let length = 1, tail = head;
    while (tail.next) {
        tail = tail.next;
        length++;
    }
    
    // Make it a circular linked list
    tail.next = head;
    
    // Find new tail: (length - k % length - 1)th node
    let newTail = head;
    for (let i = 0; i < length - (k % length) - 1; i++) {
        newTail = newTail.next;
    }
    
    // Set new head
    let newHead = newTail.next;
    newTail.next = null;
    
    return newHead;
};