class Solution {
public:
    int maxRepeating(string sequence, string word) {
        string repeated = word;
        int k = 0;
        
        while (sequence.find(repeated) != string::npos) {
            k++;
            repeated += word;
        }
        
        return k;
    }
};
