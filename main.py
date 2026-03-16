from connect4 import Connect4, PLAYER_TAKEN, IA_TAKEN
from agents import get_best_move_minimax, get_best_move_alphabeta, get_random_move
 
def demo_comparacion(depth=4):
    print("=" * 45)
    print(f"  DEMO Task 2.2 – Minimax vs Alfa-Beta (d={depth})")
    print("=" * 45)
 
    game = Connect4()
    game.drop_piece(3, PLAYER_TAKEN)
    game.drop_piece(3, IA_TAKEN)
    game.drop_piece(2, PLAYER_TAKEN)
    game.drop_piece(4, IA_TAKEN)
    game.drop_piece(2, PLAYER_TAKEN)
    game.drop_piece(5, IA_TAKEN)
    game.print_board()
 
    print("Ejecutando Minimax puro...")
    move_mm = get_best_move_minimax(game, depth)
    print(f"  → Mejor movimiento: columna {move_mm}\n")
 
    print("Ejecutando Alfa-Beta...")
    move_ab = get_best_move_alphabeta(game, depth)
    print(f"  → Mejor movimiento: columna {move_ab}")
 
    print("\nAmbos deben elegir el mismo movimiento.")
    print("Alfa-Beta visita muchos menos nodos.")
    print("=" * 45)
 
def main():
    game  = Connect4()
    depth = 5
 
    print("\n¡Bienvenido a Connect Four!")
    print(f"La IA usa Alfa-Beta con profundidad {depth}.\n")
 
    while not game.is_terminal():
        game.print_board()
 
        # Turno del jugador
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
 
        # Turno de la IA
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

def demo_vs_random(depth=5):

    print("=" * 45)
    print(" DEMO Task 2.3 – Alfa-Beta vs Random")
    print("=" * 45)

    game = Connect4()
    turn = 0

    while not game.is_terminal():

        game.print_board()

        if turn % 2 == 0:
            move = get_random_move(game)
            print(f"Random juega columna {move}")
            game.drop_piece(move, PLAYER_TAKEN)
        else:
            move = get_best_move_alphabeta(game, depth)
            print(f"IA juega columna {move}")
            game.drop_piece(move, IA_TAKEN)

        turn += 1

    game.print_board()

    if game.check_win(IA_TAKEN):
        print("La IA gana")
    elif game.check_win(PLAYER_TAKEN):
        print("Random gana")
    else:
        print("Empate")
 
 
if __name__ == "__main__":
    demo_comparacion(depth=4)
    demo_vs_random(depth=5)
    main()