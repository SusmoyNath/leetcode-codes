#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<string, vector<string>> memo; // Memoization

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        return dfs(s, wordSet);
    }

    vector<string> dfs(string s, unordered_set<string>& wordSet) {
        if (memo.count(s)) return memo[s]; // Return memoized result
        if (s.empty()) return {""}; // Base case: return empty string
        
        vector<string> result;
        for (int i = 1; i <= s.size(); i++) {
            string prefix = s.substr(0, i);
            if (wordSet.count(prefix)) { // If prefix is a valid word
                vector<string> suffixWays = dfs(s.substr(i), wordSet);
                for (string suffix : suffixWays) {
                    result.push_back(prefix + (suffix.empty() ? "" : " " + suffix));
                }
            }
        }
        return memo[s] = result; // Store result in memo
    }
};
