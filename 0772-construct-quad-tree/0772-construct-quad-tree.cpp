class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return build(grid, 0, 0, grid.size());
    }
    
    Node* build(vector<vector<int>>& grid, int row, int col, int size) {
        if (isUniform(grid, row, col, size)) {
            return new Node(grid[row][col], true);
        }
        
        int half = size / 2;
        Node* topLeft = build(grid, row, col, half);
        Node* topRight = build(grid, row, col + half, half);
        Node* bottomLeft = build(grid, row + half, col, half);
        Node* bottomRight = build(grid, row + half, col + half, half);
        
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
    
    bool isUniform(vector<vector<int>>& grid, int row, int col, int size) {
        int val = grid[row][col];
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (grid[i][j] != val) return false;
            }
        }
        return true;
    }
};
