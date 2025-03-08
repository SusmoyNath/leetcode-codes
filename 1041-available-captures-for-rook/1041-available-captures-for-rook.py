from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the position of the Rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_x, rook_y = i, j
                    break

        captures = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # Check in each direction
        for dx, dy in directions:
            x, y = rook_x, rook_y
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                if board[x][y] == 'B':  # Blocked by a bishop
                    break
                if board[x][y] == 'p':  # Capture a pawn
                    captures += 1
                    break

        return captures
