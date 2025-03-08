class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int rows = strs.size();
        int cols = strs[0].size();
        int deleteCount = 0;

        // Iterate over each column
        for (int j = 0; j < cols; j++) {
            for (int i = 1; i < rows; i++) {
                // If the column is not sorted, mark it for deletion
                if (strs[i][j] < strs[i - 1][j]) {
                    deleteCount++;
                    break;
                }
            }
        }

        return deleteCount;
    }
};
