#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> lastIndex;
        
        // Step 1: Store last occurrence of each character
        for (int i = 0; i < s.size(); i++) {
            lastIndex[s[i]] = i;
        }
        
        vector<int> result;
        int start = 0, end = 0;

        // Step 2: Traverse the string and partition
        for (int i = 0; i < s.size(); i++) {
            end = max(end, lastIndex[s[i]]); // Expand partition to include last occurrence
            
            if (i == end) { // If we reach the end of the partition
                result.push_back(end - start + 1);
                start = i + 1; // Move to next partition
            }
        }
        
        return result;
    }
};
