class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = 0, max_freq = 0, max_length = 0;
        vector<int> count(26, 0); // Frequency array

        while (right < s.size()) {
            count[s[right] - 'A']++; // Add new character to window
            max_freq = max(max_freq, count[s[right] - 'A']); 

            // If replacements needed exceed k, shrink window
            while ((right - left + 1) - max_freq > k) {
                count[s[left] - 'A']--; // Remove leftmost character
                left++;
            }

            max_length = max(max_length, right - left + 1);
            right++; // Expand window
        }

        return max_length;
    }
};
