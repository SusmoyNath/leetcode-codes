class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> result;
        int n = num.size();
        int carry = 0, i = n - 1;

        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i]; // Add the current digit to k
                i--;
            }
            result.push_back(k % 10); // Store last digit of k
            k /= 10; // Remove the last digit
        }

        reverse(result.begin(), result.end()); // Reverse to correct order
        return result;
    }
};
