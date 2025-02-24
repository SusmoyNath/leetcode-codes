class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int i = 0, n = words.size();

        while (i < n) {
            int lineLength = 0;
            int start = i;

            // Step 1: Collect words for the current line
            while (i < n && lineLength + words[i].size() + (i - start) <= maxWidth) {
                lineLength += words[i].size();
                i++;
            }

            int wordsInLine = i - start;
            int spacesNeeded = maxWidth - lineLength;
            string line = words[start];

            // Step 2: Handle space distribution
            if (wordsInLine == 1 || i == n) {
                // Left-justified (last line or only one word)
                for (int j = start + 1; j < i; j++) {
                    line += " " + words[j];
                }
                line += string(maxWidth - line.size(), ' '); // Pad extra spaces at the end
            } else {
                // Fully justified
                int spacesBetween = spacesNeeded / (wordsInLine - 1);
                int extraSpaces = spacesNeeded % (wordsInLine - 1);

                for (int j = start + 1; j < i; j++) {
                    int spacesToAdd = spacesBetween + (extraSpaces-- > 0 ? 1 : 0);
                    line += string(spacesToAdd, ' ') + words[j];
                }
            }

            result.push_back(line);
        }
        
        return result;
    }
};
