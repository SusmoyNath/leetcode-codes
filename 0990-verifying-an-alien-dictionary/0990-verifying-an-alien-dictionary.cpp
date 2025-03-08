class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        // Create a mapping of each character to its index in the alien alphabet
        unordered_map<char, int> orderMap;
        for (int i = 0; i < order.size(); i++) {
            orderMap[order[i]] = i;
        }

        // Compare each word with the next word in the list
        for (int i = 0; i < words.size() - 1; i++) {
            if (!isSorted(words[i], words[i + 1], orderMap)) {
                return false;
            }
        }
        
        return true;
    }

private:
    bool isSorted(const string& word1, const string& word2, unordered_map<char, int>& orderMap) {
        int len1 = word1.size(), len2 = word2.size();
        int minLen = min(len1, len2);

        for (int i = 0; i < minLen; i++) {
            if (orderMap[word1[i]] < orderMap[word2[i]]) {
                return true; // word1 is lexicographically smaller
            }
            if (orderMap[word1[i]] > orderMap[word2[i]]) {
                return false; // word1 is greater, so words are not sorted
            }
        }

        // If we reach here, words are identical up to minLen; the shorter word should come first
        return len1 <= len2;
    }
};
