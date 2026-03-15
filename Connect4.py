import numpy as np

ROWS = 6
COLS = 7
EMPTY_SPACE = 0
PLAYER_TAKEN = 1
IA_TAKEN = 2

class Connect4:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)

    def print_board(self):
        print(f"\n{np.flip(self.board, 0)}\n")

    def get_valid_moves(self):
        valid_moves = []
        for col in range(COLS):
            if self.board[ROWS-1][col] == EMPTY_SPACE:
                valid_moves.append(col)
        return valid_moves
    
    def drop_piece(self, col, piece):
        for r in range(ROWS):
            if self.board[r][col] == EMPTY_SPACE:
                self.board[r][col] = piece
                break
    
    def copy(self):
        new_game = Connect4()
        new_game.board = np.copy(self.board)
        return new_game
    
    def check_win(self, piece):
        # Horizontal
        for row in range(ROWS):
            for col in range(COLS - 3):
                if np.all(self.board[row, col:col+4] == piece):
                    return True

        # Vertical
        for col in range(COLS):
            for row in range(ROWS - 3):
                if np.all(self.board[row:row+4, col] == piece):
                    return True

        # Diagonal para arriba
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self.board[row+i][col+i] == piece for i in range(4)):
                    return True

        # Diagonal para abajo
        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if all(self.board[row-i][col+i] == piece for i in range(4)):
                    return True

        return False
    
    def is_terminal(self):
        return self.check_win(PLAYER_TAKEN) or self.check_win(IA_TAKEN) or len(self.get_valid_moves()) == 0
        


if __name__ == '__main__':
    c = Connect4()
    c.print_board()
    c.drop_piece(2, PLAYER_TAKEN)
    c.drop_piece(2, PLAYER_TAKEN)
    c.drop_piece(2, PLAYER_TAKEN)
    c.drop_piece(2, PLAYER_TAKEN)
    print(c.get_valid_moves())
    print("Jugador gana: ",c.check_win(PLAYER_TAKEN))
    print("IA gana: ", c.check_win(IA_TAKEN))
    c.print_board()