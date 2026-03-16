from Connect4 import Connect4, PLAYER_TAKEN, IA_TAKEN, ROWS, COLS, EMPTY_SPACE

WIN_SCORE = 1000
LOSE_SCORE = -1000
DRAW_SCORE = 0

nodes_visited = 0

def minimax(game: Connect4, depth, maximizing_player):
    global nodes_visited
    nodes_visited += 1

    valid_moves = game.get_valid_moves()
    terminal = game.is_terminal()

    if depth == 0 or terminal:
        if terminal:
            if game.check_win(IA_TAKEN):
                return WIN_SCORE
            elif game.check_win(PLAYER_TAKEN):
                return LOSE_SCORE
            else:
                return DRAW_SCORE
        return 0

    if maximizing_player:
        value = -float("inf")
        for col in valid_moves:
            new_game = game.copy()
            new_game.drop_piece(col, IA_TAKEN)
            value = max(value, minimax(new_game, depth-1, False))
        return value

    else:
        value = float("inf")
        for col in valid_moves:
            new_game = game.copy()
            new_game.drop_piece(col, PLAYER_TAKEN)
            value = min(value, minimax(new_game, depth-1, True))
        return value
    
def get_best_move_minimax(game: Connect4, depth):
    global nodes_visited
    nodes_visited = 0

    valid_moves = game.get_valid_moves()
    best_score = -float("inf")
    best_move = None

    for col in valid_moves:
        new_game = game.copy()
        new_game.drop_piece(col, IA_TAKEN)
        score = minimax(new_game, depth-1, False)
        if score > best_score:
            best_score = score
            best_move = col

    print("Nodos visitados:", nodes_visited)
    return best_move

def _score_window(window, piece):
    """Puntúa una ventana de 4 celdas desde la perspectiva de 'piece'."""
    opp = PLAYER_TAKEN if piece == IA_TAKEN else IA_TAKEN
 
    count_piece = window.count(piece)
    count_empty = window.count(EMPTY_SPACE)
    count_opp   = window.count(opp)
 
    score = 0
 
    if count_piece == 3 and count_empty == 1:
        score += 50                 
    elif count_piece == 2 and count_empty == 2:
        score += 10                

    if count_opp == 3 and count_empty == 1:
        score -= 80                
 
    return score
 
 
def evaluate(game: Connect4, piece):
    board = game.board
    score = 0
    center_col = [int(board[r][COLS // 2]) for r in range(ROWS)]
    score += center_col.count(piece) * 6

    for r in range(ROWS):
        row_array = [int(board[r][c]) for c in range(COLS)]
        for c in range(COLS - 3):
            window = row_array[c: c + 4]
            score += _score_window(window, piece)

    for c in range(COLS):
        col_array = [int(board[r][c]) for r in range(ROWS)]
        for r in range(ROWS - 3):
            window = col_array[r: r + 4]
            score += _score_window(window, piece)

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [int(board[r + i][c + i]) for i in range(4)]
            score += _score_window(window, piece)

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [int(board[r - i][c + i]) for i in range(4)]
            score += _score_window(window, piece)
 
    return score

def alphabeta(game: Connect4, depth, alpha, beta, maximizing_player):
    global nodes_visited
    nodes_visited += 1
 
    valid_moves = game.get_valid_moves()
    terminal = game.is_terminal()
 
    if depth == 0 or terminal:
        if terminal:
            if game.check_win(IA_TAKEN):
                return WIN_SCORE
            elif game.check_win(PLAYER_TAKEN):
                return LOSE_SCORE
            else:
                return DRAW_SCORE

        return evaluate(game, IA_TAKEN)

    if maximizing_player:
        value = -float("inf")
        for col in valid_moves:
            new_game = game.copy()
            new_game.drop_piece(col, IA_TAKEN)
            value = max(value, alphabeta(new_game, depth-1, alpha, beta, False))
 
            alpha = max(alpha, value)   
 
            if alpha >= beta:       
                break
 
        return value
 
    else:
        value = float("inf")
        for col in valid_moves:
            new_game = game.copy()
            new_game.drop_piece(col, PLAYER_TAKEN)
            value = min(value, alphabeta(new_game, depth-1, alpha, beta, True))
 
            beta = min(beta, value)  
 
            if alpha >= beta:          
                break
 
        return value
 
 
def get_best_move_alphabeta(game: Connect4, depth):
    global nodes_visited
    nodes_visited = 0
 
    valid_moves = game.get_valid_moves()
    best_score = -float("inf")
    best_move = None

    alpha = -float("inf")
    beta  =  float("inf")
 
    for col in valid_moves:
        new_game = game.copy()
        new_game.drop_piece(col, IA_TAKEN)
        score = alphabeta(new_game, depth-1, alpha, beta, False)
        if score > best_score:
            best_score = score
            best_move = col
        alpha = max(alpha, best_score)
 
    print("Nodos visitados (Alfa-Beta):", nodes_visited)
    return best_move
