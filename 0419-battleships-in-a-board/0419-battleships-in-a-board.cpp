class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check if it's the start of a battleship
                if (board[i][j] == 'X' &&
                    (i == 0 || board[i - 1][j] == '.') &&  // No 'X' above
                    (j == 0 || board[i][j - 1] == '.')) {  // No 'X' to the left
                    count++;
                }
            }
        }
        return count;
    }
};
