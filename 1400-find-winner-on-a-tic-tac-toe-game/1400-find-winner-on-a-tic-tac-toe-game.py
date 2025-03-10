from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["" for _ in range(3)] for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            board[r][c] = "A" if i % 2 == 0 else "B"
        
        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        if check_winner("A"): return "A"
        if check_winner("B"): return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"