class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        return accumulate(word1.begin(), word1.end(), string()) == 
               accumulate(word2.begin(), word2.end(), string());
    }
};
