#include <stack>

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        std::stack<int> s1, s2;

        // Push elements of l1 into stack
        while (l1) {
            s1.push(l1->val);
            l1 = l1->next;
        }

        // Push elements of l2 into stack
        while (l2) {
            s2.push(l2->val);
            l2 = l2->next;
        }

        ListNode* result = nullptr; // Head of the result list
        int carry = 0;

        // Process stacks
        while (!s1.empty() || !s2.empty() || carry) {
            int sum = carry;
            
            if (!s1.empty()) {
                sum += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                sum += s2.top();
                s2.pop();
            }

            carry = sum / 10;
            sum %= 10;

            // Insert the new node at the head (since we process from least to most significant)
            ListNode* newNode = new ListNode(sum);
            newNode->next = result;
            result = newNode;
        }

        return result;
    }
};
