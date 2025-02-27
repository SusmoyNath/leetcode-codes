class Solution {
public:
    unordered_set<string> wordSet;
    unordered_map<string, bool> memo;
    
    bool isConcatenated(string word) {
        if (memo.count(word)) return memo[word];

        int n = word.size();
        for (int i = 1; i < n; ++i) {
            string prefix = word.substr(0, i);
            string suffix = word.substr(i);
            
            if (wordSet.count(prefix) && (wordSet.count(suffix) || isConcatenated(suffix))) {
                return memo[word] = true;
            }
        }
        
        return memo[word] = false;
    }

    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        vector<string> result;
        wordSet = unordered_set<string>(words.begin(), words.end());
        
        for (string& word : words) {
            if (word.empty()) continue;
            wordSet.erase(word);  // Avoid self-checking
            if (isConcatenated(word)) {
                result.push_back(word);
            }
            wordSet.insert(word);
        }
        
        return result;
    }
};
