class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.size()) return "0"; // If we remove all digits, return "0"

        stack<char> s;
        for (char digit : num) {
            // Remove digits from the stack if they are greater than the current digit
            while (!s.empty() && k > 0 && s.top() > digit) {
                s.pop();
                k--;
            }
            s.push(digit);
        }

        // Remove remaining `k` digits from the end if necessary
        while (k > 0 && !s.empty()) {
            s.pop();
            k--;
        }

        // Build the final result
        string result;
        while (!s.empty()) {
            result += s.top();
            s.pop();
        }

        // Reverse the result since we used a stack
        reverse(result.begin(), result.end());

        // Remove leading zeros
        int i = 0;
        while (i < result.size() && result[i] == '0') i++;
        result = result.substr(i);

        // If the result is empty, return "0"
        return result.empty() ? "0" : result;
    }
};
