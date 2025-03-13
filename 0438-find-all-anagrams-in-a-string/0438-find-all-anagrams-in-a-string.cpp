#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.size() < p.size()) return result;  // Edge case
        
        vector<int> pCount(26, 0), sCount(26, 0);
        
        // Count frequency of characters in p
        for (char c : p) {
            pCount[c - 'a']++;
        }
        
        int windowSize = p.size();
        
        // First window in s
        for (int i = 0; i < windowSize; i++) {
            sCount[s[i] - 'a']++;
        }
        
        // Compare initial window
        if (sCount == pCount) result.push_back(0);
        
        // Sliding window
        for (int i = windowSize; i < s.size(); i++) {
            sCount[s[i] - 'a']++;  // Add new character to window
            sCount[s[i - windowSize] - 'a']--;  // Remove old character from window
            
            if (sCount == pCount) {
                result.push_back(i - windowSize + 1);  // Store start index
            }
        }
        
        return result;
    }
};
