class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return nullptr;  // Edge case: empty list

        stack<Node*> st;
        Node* curr = head;
        
        while (curr) {
            if (curr->child) {
                // If next node exists, push it to stack
                if (curr->next) st.push(curr->next);
                
                // Connect child as next node
                curr->next = curr->child;
                curr->next->prev = curr;
                curr->child = nullptr;
            }

            // If at the end of a level, pop from stack
            if (!curr->next && !st.empty()) {
                curr->next = st.top();
                st.top()->prev = curr;
                st.pop();
            }
            
            curr = curr->next;
        }
        
        return head;
    }
};
