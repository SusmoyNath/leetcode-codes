#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <cctype>

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> bannedSet(banned.begin(), banned.end());
        unordered_map<string, int> wordCount;
        string word, result;
        int maxCount = 0;

        // Convert paragraph to lowercase and replace punctuation with spaces
        for (char &c : paragraph) {
            if (isalpha(c)) c = tolower(c);
            else c = ' ';
        }

        // Use stringstream to extract words
        stringstream ss(paragraph);
        while (ss >> word) {
            if (!bannedSet.count(word)) {
                wordCount[word]++;
                if (wordCount[word] > maxCount) {
                    maxCount = wordCount[word];
                    result = word;
                }
            }
        }

        return result;
    }
};
