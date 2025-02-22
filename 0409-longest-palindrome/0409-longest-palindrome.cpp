#include <unordered_map>

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> freq;
        
        // Count character frequencies
        for (char c : s) {
            freq[c]++;
        }
        
        int length = 0;
        bool hasOdd = false;
        
        for (auto& [ch, count] : freq) {
            length += (count / 2) * 2;  // Add even part of count
            if (count % 2 == 1) {
                hasOdd = true;  // Mark that an odd character exists
            }
        }
        
        // If there's any odd count, we can place one in the center
        if (hasOdd) {
            length++;
        }
        
        return length;
    }
};
