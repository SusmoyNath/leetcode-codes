#include <vector>
#include <string>

class Solution {
public:
    int findSubstringInWraproundString(std::string s) {
        std::vector<int> dp(26, 0);  // dp[i] stores the longest substring ending at 'a' + i
        int maxLength = 0;  // Tracks the length of the current increasing substring

        for (int i = 0; i < s.size(); ++i) {
            if (i > 0 && (s[i] - s[i - 1] == 1 || (s[i - 1] == 'z' && s[i] == 'a'))) {
                maxLength++;  // Extend the consecutive sequence
            } else {
                maxLength = 1;  // Reset if sequence breaks
            }

            int index = s[i] - 'a';
            dp[index] = std::max(dp[index], maxLength);  // Store max length for each character
        }

        // Sum of all dp[i] values gives the total unique substrings
        return std::accumulate(dp.begin(), dp.end(), 0);
    }
};
