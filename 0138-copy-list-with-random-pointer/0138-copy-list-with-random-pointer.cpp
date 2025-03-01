class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        // Step 1: Clone nodes and interweave them
        Node* cur = head;
        while (cur) {
            Node* clone = new Node(cur->val);
            clone->next = cur->next;
            cur->next = clone;
            cur = clone->next;
        }

        // Step 2: Assign random pointers to cloned nodes
        cur = head;
        while (cur) {
            if (cur->random) {
                cur->next->random = cur->random->next;
            }
            cur = cur->next->next;
        }

        // Step 3: Separate the two lists
        Node* newHead = head->next;
        Node* copy = newHead;
        cur = head;
        while (cur) {
            cur->next = cur->next->next;
            if (copy->next) {
                copy->next = copy->next->next;
            }
            cur = cur->next;
            copy = copy->next;
        }

        return newHead;
    }
};
