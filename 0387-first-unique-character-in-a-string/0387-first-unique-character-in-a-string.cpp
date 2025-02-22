class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> freq(26, 0);  // Array to store frequency of letters (a-z)
        
        // Count frequency of each character in the string
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        // Find the first character with frequency 1
        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i] - 'a'] == 1) return i;
        }
        
        return -1;  // No unique character found
    }
};