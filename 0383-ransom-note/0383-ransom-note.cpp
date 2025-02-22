class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> freq(26, 0);  // Array to store frequency of letters (a-z)

        for (char c : magazine) {
            freq[c - 'a']++;  // Count letters in magazine
        }

        for (char c : ransomNote) {
            if (freq[c - 'a'] == 0) return false;  // Not enough letters available
            freq[c - 'a']--;  // Use one letter from magazine
        }

        return true;
    }
};