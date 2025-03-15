class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> result(n, 0);
        
        if (k == 0) return result; // If k == 0, return all zeros
        
        vector<int> extended(code.begin(), code.end()); // Duplicate array for circular indexing
        extended.insert(extended.end(), code.begin(), code.end()); // Extend the array
        
        int start = (k > 0) ? 1 : n + k; // Starting index for window sum
        int end = (k > 0) ? k : n - 1;   // Ending index for window sum

        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += extended[i];
        }

        for (int i = 0; i < n; i++) {
            result[i] = sum;
            sum -= extended[start]; // Remove outgoing element
            start++;  // Move start forward
            end++;    // Move end forward
            sum += extended[end];  // Add new incoming element
        }
        
        return result;
    }
};
