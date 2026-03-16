from Connect4 import Connect4, PLAYER_TAKEN, IA_TAKEN
from agents import get_best_move_alphabeta
 
def main():
    game  = Connect4()
    depth = 5   # Profundidad recomendada
 
    print("\n¡Bienvenido a Connect Four!")
    print(f"La IA usa Alfa-Beta con profundidad {depth}.\n")
 
    while not game.is_terminal():
        game.print_board()
 
        valid = game.get_valid_moves()
        col = -1
        while col not in valid:
            try:
                col = int(input(f"Tu movimiento {valid}: "))
            except ValueError:
                pass
 
        game.drop_piece(col, PLAYER_TAKEN)
 
        if game.is_terminal():
            break

        ai_move = get_best_move_alphabeta(game, depth)
        print(f"Turno de la IA → columna {ai_move}")
        game.drop_piece(ai_move, IA_TAKEN)

    game.print_board()
    if game.check_win(PLAYER_TAKEN):
        print("¡Ganaste!")
    elif game.check_win(IA_TAKEN):
        print("La IA gana.")
    else:
        print("Empate.")
 
 
if __name__ == "__main__":
    main()
