#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<string>> result;
    
    void backtrack(int row, int n, vector<string>& board, 
                   unordered_set<int>& cols, 
                   unordered_set<int>& diag1, 
                   unordered_set<int>& diag2) {
        if (row == n) {
            result.push_back(board); // Found a valid configuration
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.count(col) || diag1.count(row - col) || diag2.count(row + col)) {
                continue; // Skip invalid positions
            }

            // Place queen
            board[row][col] = 'Q';
            cols.insert(col);
            diag1.insert(row - col);
            diag2.insert(row + col);

            // Recur for the next row
            backtrack(row + 1, n, board, cols, diag1, diag2);

            // Backtrack: Remove the queen
            board[row][col] = '.';
            cols.erase(col);
            diag1.erase(row - col);
            diag2.erase(row + col);
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.')); // Initialize empty board
        unordered_set<int> cols, diag1, diag2; // Track used columns and diagonals
        backtrack(0, n, board, cols, diag1, diag2);
        return result;
    }
};
