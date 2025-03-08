class Solution {
public:
    int calculate(string s) {
        int n = s.size();
        stack<int> stk;
        char op = '+';  // Stores the last encountered operator
        int num = 0;     // Stores the current number
        
        for (int i = 0; i < n; i++) {
            if (isdigit(s[i])) {
                num = num * 10 + (s[i] - '0');  // Build the number
            }
            
            // Process if we hit an operator or the last character
            if ((!isdigit(s[i]) && s[i] != ' ') || i == n - 1) {
                if (op == '+') {
                    stk.push(num);
                } else if (op == '-') {
                    stk.push(-num);
                } else if (op == '*') {
                    int top = stk.top();
                    stk.pop();
                    stk.push(top * num);
                } else if (op == '/') {
                    int top = stk.top();
                    stk.pop();
                    stk.push(top / num);
                }
                // Update `op` and reset `num`
                op = s[i];
                num = 0;
            }
        }
        
        // Sum up values in stack
        int result = 0;
        while (!stk.empty()) {
            result += stk.top();
            stk.pop();
        }
        return result;
    }
};
