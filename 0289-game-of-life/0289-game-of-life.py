from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        
        # Neighbor directions (8 directions: horizontal, vertical, diagonal)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Step 1: Apply rules and encode states
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                
                # Count live neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1
                
                # Apply rules using state encoding
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Live â Dead
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2   # Dead â Live
        
        # Step 2: Decode the board to the final state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  # Convert -1 â 0
                if board[r][c] == 2:
                    board[r][c] = 1  # Convert 2 â 1
