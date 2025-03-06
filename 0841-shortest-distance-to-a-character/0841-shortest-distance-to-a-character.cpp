#include <vector>
#include <string>
#include <climits>

class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.size();
        vector<int> answer(n, INT_MAX);
        int pos = -n;  // Initialize with a large negative number

        // Left to right pass
        for (int i = 0; i < n; i++) {
            if (s[i] == c) pos = i;
            answer[i] = abs(i - pos);
        }

        // Right to left pass
        pos = 2 * n;  // Initialize with a large positive number
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == c) pos = i;
            answer[i] = std::min(answer[i], abs(i - pos));
        }

        return answer;
    }
};
