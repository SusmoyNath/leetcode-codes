class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head; // Edge case: no reversal needed

        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *prev = dummy, *curr = dummy, *next = dummy;

        int count = 0;
        while (curr->next) {  // Count total nodes
            curr = curr->next;
            count++;
        }

        while (count >= k) {  // Reverse in k-groups
            curr = prev->next;
            next = curr->next;
            for (int i = 1; i < k; i++) {
                curr->next = next->next;
                next->next = prev->next;
                prev->next = next;
                next = curr->next;
            }
            prev = curr;
            count -= k;
        }

        return dummy->next;
    }
};
