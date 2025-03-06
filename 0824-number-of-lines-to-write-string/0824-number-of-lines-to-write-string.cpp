class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1, current_width = 0;

        for (char c : s) {
            int width = widths[c - 'a'];  // Get the width of the character
            
            if (current_width + width > 100) {  // Start a new line if it exceeds 100
                lines++;
                current_width = width;
            } else {
                current_width += width;
            }
        }

        return {lines, current_width};
    }
};
