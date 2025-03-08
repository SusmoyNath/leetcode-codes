class Solution {
public:
    vector<int> diStringMatch(string s) {
        int n = s.size();
        vector<int> result;
        int low = 0, high = n; // Using two pointers
        
        for (char c : s) {
            if (c == 'I') {
                result.push_back(low++);
            } else { // 'D'
                result.push_back(high--);
            }
        }
        
        result.push_back(low); // The last remaining number
        return result;
    }
};
