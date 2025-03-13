#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int write = 0;  // Write pointer
        int i = 0;  // Read pointer

        while (i < chars.size()) {
            char currentChar = chars[i];
            int count = 0;

            // Count occurrences of the current character
            while (i < chars.size() && chars[i] == currentChar) {
                count++;
                i++;
            }

            // Write the character
            chars[write++] = currentChar;

            // Write the count if more than 1
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[write++] = c;
                }
            }
        }

        return write;  // New length of the compressed array
    }
};
