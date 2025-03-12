import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result, node, index = None, self.head, 1
        
        while node:
            # Pick current node with probability 1/index
            if random.randint(1, index) == 1:
                result = node.val
            node = node.next
            index += 1
        
        return result
