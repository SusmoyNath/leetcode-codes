class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";

        unordered_map<char, int> tCount, windowCount;
        for (char c : t) tCount[c]++; // Count frequency of chars in t

        int left = 0, right = 0, minLength = INT_MAX, minStart = 0;
        int required = tCount.size();  // Number of unique chars in t
        int formed = 0;  // Tracks how many chars have the required count

        while (right < s.size()) {
            char c = s[right];
            windowCount[c]++;

            if (tCount.find(c) != tCount.end() && windowCount[c] == tCount[c]) {
                formed++;
            }

            // Try shrinking the window
            while (formed == required) {
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    minStart = left;
                }

                char leftChar = s[left];
                windowCount[leftChar]--;

                if (tCount.find(leftChar) != tCount.end() && windowCount[leftChar] < tCount[leftChar]) {
                    formed--;
                }
                
                left++; // Shrink the window
            }

            right++; // Expand the window
        }

        return minLength == INT_MAX ? "" : s.substr(minStart, minLength);
    }
};
