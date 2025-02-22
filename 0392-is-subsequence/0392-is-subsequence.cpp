class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        
        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) {
                i++;  // Move to the next character in s
            }
            j++;  // Always move in t
        }
        
        return i == s.size(); // If we matched all characters in s, return true
    }
};