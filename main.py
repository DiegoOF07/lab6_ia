from connect4 import Connect4, PLAYER_TAKEN, IA_TAKEN
from agents import get_best_move_minimax


def main():

    game = Connect4()

    while not game.is_terminal():
        game.print_board()

        col = int(input("Tu movimiento (0-6): "))
        game.drop_piece(col, PLAYER_TAKEN)

        ai_move = get_best_move_minimax(game, depth=3)
        print("Turno de la IA:", ai_move)

        game.drop_piece(ai_move, IA_TAKEN)


if __name__ == "__main__":
    main()