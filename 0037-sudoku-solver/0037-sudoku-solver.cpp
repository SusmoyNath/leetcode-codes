#include <vector>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }

private:
    bool isValid(vector<vector<char>>& board, int row, int col, char num) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num) return false; // Check row
            if (board[i][col] == num) return false; // Check column
            if (board[(row / 3) * 3 + i / 3][(col / 3) * 3 + i % 3] == num) return false; // Check 3x3 grid
        }
        return true;
    }

    bool solve(vector<vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') { // Found an empty cell
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValid(board, row, col, num)) {
                            board[row][col] = num; // Place the number
                            if (solve(board)) return true; // Solve the rest of the board
                            board[row][col] = '.'; // Backtrack
                        }
                    }
                    return false; // No valid number found, trigger backtracking
                }
            }
        }
        return true; // Solved
    }
};
