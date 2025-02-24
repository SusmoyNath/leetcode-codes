#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return {}; // Early exit if `endWord` is not present

        unordered_map<string, vector<string>> adjList; // Stores possible paths
        unordered_map<string, int> depth; // Tracks shortest path depth
        queue<string> q;
        q.push(beginWord);
        depth[beginWord] = 1;
        int level = 1;
        bool found = false;

        while (!q.empty() && !found) {
            int size = q.size();
            unordered_set<string> visited;

            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                string original = word;

                for (int j = 0; j < word.size(); j++) {
                    char originalChar = word[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == originalChar) continue;
                        word[j] = c;
                        if (wordSet.count(word)) {
                            if (depth.count(word) == 0) {
                                depth[word] = level + 1;
                                q.push(word);
                                visited.insert(word);
                            }
                            if (depth[word] == level + 1) {
                                adjList[word].push_back(original);
                            }
                            if (word == endWord) found = true;
                        }
                    }
                    word[j] = originalChar;
                }
            }
            for (const string& w : visited) wordSet.erase(w); // Avoid re-visiting
            level++;
        }

        vector<vector<string>> results;
        if (found) {
            vector<string> path = {endWord};
            backtrack(endWord, beginWord, adjList, path, results);
        }
        return results;
    }

private:
    void backtrack(string word, string& beginWord, unordered_map<string, vector<string>>& adjList, vector<string>& path, vector<vector<string>>& results) {
        if (word == beginWord) {
            reverse(path.begin(), path.end());
            results.push_back(path);
            reverse(path.begin(), path.end());
            return;
        }
        for (string& prev : adjList[word]) {
            path.push_back(prev);
            backtrack(prev, beginWord, adjList, path, results);
            path.pop_back();
        }
    }
};
