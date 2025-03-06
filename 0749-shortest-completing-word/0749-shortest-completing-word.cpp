#include <vector>
#include <string>
#include <unordered_map>
#include <cctype>
using namespace std;

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        unordered_map<char, int> required;
        
        // Process licensePlate to extract letter frequencies
        for (char c : licensePlate) {
            if (isalpha(c)) {
                required[tolower(c)]++;
            }
        }
        
        string result;
        int minLength = INT_MAX;
        
        // Check each word in words
        for (const string& word : words) {
            unordered_map<char, int> wordFreq;
            for (char c : word) {
                wordFreq[c]++;
            }
            
            // Verify if the word satisfies required letter counts
            bool valid = true;
            for (const auto& [ch, count] : required) {
                if (wordFreq[ch] < count) {
                    valid = false;
                    break;
                }
            }
            
            // Update result if this word is shorter and valid
            if (valid && word.length() < minLength) {
                minLength = word.length();
                result = word;
            }
        }
        
        return result;
    }
};