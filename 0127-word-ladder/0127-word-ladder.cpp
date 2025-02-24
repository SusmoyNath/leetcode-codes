#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return 0; // If endWord is not in wordList, no transformation is possible

        unordered_set<string> frontSet, backSet, tempSet;
        frontSet.insert(beginWord);
        backSet.insert(endWord);
        int step = 1;

        while (!frontSet.empty() && !backSet.empty()) {
            if (frontSet.size() > backSet.size()) swap(frontSet, backSet); // Expand the smaller set

            tempSet.clear();
            for (string word : frontSet) {
                string original = word;
                for (int i = 0; i < word.size(); i++) {
                    char oldChar = word[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == oldChar) continue;
                        word[i] = c;
                        if (backSet.count(word)) return step + 1; // If paths meet, return steps
                        if (wordSet.count(word)) {
                            tempSet.insert(word);
                            wordSet.erase(word); // Remove visited word to avoid loops
                        }
                    }
                    word[i] = oldChar;
                }
            }
            swap(frontSet, tempSet);
            step++;
        }
        return 0; // No path found
    }
};
