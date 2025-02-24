class Solution {
public:
    int count = 0;

    void backtrack(int row, int n, int cols, int diag1, int diag2) {
        if (row == n) {
            count++;
            return;
        }

        // Available positions (bitmask)
        int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);

        while (available) {
            int pos = available & -available; // Get the rightmost 1-bit
            available -= pos; // Remove this position from available spots

            // Recursive call with updated constraints
            backtrack(row + 1, n, cols | pos, (diag1 | pos) << 1, (diag2 | pos) >> 1);
        }
    }

    int totalNQueens(int n) {
        backtrack(0, n, 0, 0, 0);
        return count;
    }
};
