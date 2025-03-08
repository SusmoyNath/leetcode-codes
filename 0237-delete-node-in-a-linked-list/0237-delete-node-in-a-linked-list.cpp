class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;  // Step 1: Copy next node's value
        ListNode* temp = node->next;  // Step 2: Store the next node
        node->next = node->next->next; // Step 3: Skip the next node
        delete temp; // Step 4: Free memory
    }
};
